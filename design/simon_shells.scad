$fn=64;

// All dimensions in mm
ro=60;                             // outer radius of sphere
wall_thick=3;
ifr_width=10;                       // width of if ring
ifr_height=7;                       // height of if ring
rc=5;                               // corner radius
lip=5;                              // height of lip on if ring
gap=0.5;                            // gap for "lip" slit of back shell

ear_r=10;                           // radius of ear
ear_h=10;                           // height of ear

rf=35;                              // radius of face plate in front shell
display_size=[36.5,47.5];           // display size    

// build SIMON
boxsize=2.1*ro;
//boxsize=0;
cutopen(boxsize) front_shell();
cutopen(boxsize) back_shell();


// -------------------------------------------------------------------------------------------------

module front_shell() {
    a=asin(rf/ro);
    dx=ro*cos(a);
    echo(dx);
    union() {
        // half sphere with cut-out for face
        difference() {
            halfsphere();
            rotate([0,90,0]) cylinder(r1=0, r2=rf*ro/dx, h=ro);
        }
        // face plate with cut-out for display
        difference() {
            intersection() {
                translate([dx,0,0]) rotate([0,270,0]) cylinder(r=ro, h=wall_thick);
                sphere(ro);
            }
            //translate([ro/2,0,0]) cube([ro,display_size[1],display_size[0]], center=true);
            translate([dx-wall_thick,0,0]) rotate([0,90,0]) linear_extrude(wall_thick, scale=1.05)
                square([display_size[0],display_size[1]], center=true);
            
        }
        // if ring lip
        intersection() {
            rotate([0,270,0]) rotate_extrude() translate([ro-wall_thick,0,0])
                square([wall_thick,lip]);
            sphere(ro);
        }
        // ears
        ears();
    }
}

module back_shell() {
    difference() {
        // half sphere
        mirror([1,0,0]) halfsphere();
        // if ring lip cut-out
        rotate([0,270,0]) rotate_extrude()
            translate([ro-wall_thick-gap,0,0]) square([2*wall_thick,5]);
        rotate([0,270,0]) cylinder(h=gap, r=1.1*ro);
        // ears
        ears_cutout();
    }
}

module cutopen(boxsize=2.1*ro) {
    difference() {
        children();
        translate([0,-boxsize/2,0]) cube(size=boxsize, center=true);
    }    
}

// Function to mirror and copy and object at the same time
// Reference: https://forum.openscad.org/Wish-mirror-copy-true-tp10681p10683.html
module copymirror(vec) {
    children();
    mirror(vec) children();
}

module ears() {
    copymirror([0,1,0]) difference() {
        // the cylindrical ears
        translate([0,ro-lip/2,0]) rotate([270,0,0]) cylinder(h=ear_h,r=ear_r, center=true);
        // substract inner sphere
        sphere(ro-wall_thick);
        // substract lip for good fit
        rotate([0,270,0]) cylinder(h=ro,r=ro-wall_thick);
    }    
}

module ears_cutout() {
    copymirror([0,1,0]) difference() {
        // the cylindrical ears
        translate([0,ro-lip/2,0]) rotate([270,0,0]) cylinder(h=ear_h,r=ear_r+gap, center=true);
        // substract inner sphere
        sphere(ro-wall_thick-gap);
    }    
}

module halfsphere() {
    union() {
        // main hollow half sphere
        difference() {
            sphere(ro);
            sphere(ro-wall_thick);
            translate([-ro/2,0,0]) cube([ro,2*ro,2*ro], center=true);
        }
        // if ring
        intersection() {
            rotate([0,90,0]) linear_extrude(ifr_height) difference() {
                circle(ro);
                circle(ro-ifr_width);
            }
            sphere(ro);
        }
        // filleting the ring to the half sphere
        translate([ifr_height,0,0]) rotate([0,90,0]) {
            rotate_extrude() translate([-(ro-wall_thick),0,0]) difference() {
                square(rc);
                translate([rc,rc,0]) circle(rc);
            }
        }
    }
}