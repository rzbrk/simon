$fn=128;

ro=20;                      // outer diameter of sphere
wt=1;                       // wall thickness
rf=13;                      // radius of face
bp=10;                      // size of back pack
sep=0.01;                     // separation of half spheres
displ=[20,13];              // display size
ws=[12,10];                 // wing size
ebox=[15,20,20];            // size of electr. box    

translate([sep/2,0,0]) color("LightBlue") { front_half_sphere(); }
translate([-sep/2,0,0]) color("Lime") { back_half_sphere(); }
translate([0,0,0]) color("OrangeRed") { cube(ebox, center=true); }

module front_half_sphere() {
    a=asin(rf/ro);
    dx=ro*cos(a);
    union() {
        // Half sphere with cut-out for face
        difference() {
            hollow_half_sphere();
            rotate([0,90,0]) cylinder(r1=0, r2=rf*ro/dx, h=ro);
        }
        // face plate with display
        difference() {
            intersection() {
                translate([dx,0,0]) rotate([0,270,0]) cylinder(r=ro, h=wt);
                sphere(ro);
            }
            translate([dx,0,0]) cube([wt,displ[0],displ[1]], center=true);
        }
        // wings
        translate([0,ro-wt,0]) rotate([0,-45,0]) wing();
        mirror([0,1,0]) translate([0,ro-wt,0]) rotate([0,-45,0]) wing();
    }
}

module back_half_sphere() {
    a=asin(rf/ro);
    dx=ro*cos(a);
    a2=asin(bp/ro);
    dx2=ro*cos(a2);
    union() {
        // Half sphere with cut-out for "back pack" and wings
        difference() {
            mirror([1,0,0]) hollow_half_sphere();
            translate([-bp,0,0]) cube(2*(bp-wt), center=true);
            //wings
            translate([0,ro-wt,0]) rotate([0,-45,0]) wing();
            mirror([0,1,0]) translate([0,ro-wt,0]) rotate([0,-45,0]) wing();
        }
        // "Back back"
        difference() {
            translate([-dx2,0,0]) cube([bp,2*bp,2*bp], center=true);
            translate([-dx2+wt,0,0]) cube([bp-wt,2*(bp-wt),2*(bp-wt)], center=true);
            sphere(ro-wt);
        }
        // Nozzle
        translate([-dx-rf/2,0,0]) rotate([0,270,0]) cylinder(r1=ro/10, r2=ro/4, h=ro/2);
    }
}

module wing() {
    rotate([0,90,90]) {
        cylinder(r=ro/8, h=2*wt);
        cylinder(r=wt/2, h=ro/4);
    }
    translate([0,ro/4+ws[0]/2,0]) cube([wt, ws[0], ws[1]], center=true);
}

module hollow_half_sphere() {
    difference() {
        sphere(ro);
        sphere(ro-wt);
        translate([-2*ro,-ro,-ro]) cube(2*ro);
    }
}
