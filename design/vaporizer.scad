$fn=100;

// all dimensions in mm
dfan=30;                    // diameter of fan
dfanscr=3;                  // diameter of screw holes in fan
rc=3;                       // corner radius
wt=2;                       // wall thickness

dlid=45;                    // diameter of lid
hlid=9;                     // height of lid
tilt=45;                    // tilt angle of glass jar
din=20;                     // diameter hole inflow
dout=16;                    // diameter hoile outflow/exhaust
offset=8;                   // offset of holes in lid
dcable=3;                   // diameter for holes for cables

sep=20;                     // separation of fan and lid mount


union() {
    fan_mount(dhole=dfan-2*wt);
    translate([0,0,-sep]) lid_mount();
    fan_tube();

    translate([11,0,-23.3]) rotate([0,90,0]) linear_extrude(10) difference() {
                circle(d=dout);
                circle(d=dout-2*wt);
    }

    translate([20,0,-23.3]) rotate([0,90,0]) fan_mount(dout-2*wt);

    rotate([90,0,0]) translate([0,0,-wt/2]) linear_extrude(wt) {
        polygon([[15,0],[21,-10],[21,-17],[5,-17],[0,-22]]);
        polygon([[10,-30],[20,-30],[20,-37],[15,-37]]);
        polygon([[-15,0],[-18,-5],[-12,-9]]);
    }
}

// ===================================================================================

module fan_mount(dhole) {
    linear_extrude(1.5*wt) difference() {
        // mounting plate for fan
        hull() {
            translate([dfan/2-rc,dfan/2-rc,0]) circle(rc);
            translate([-dfan/2+rc,dfan/2-rc,0]) circle(rc);
            translate([-dfan/2+rc,-dfan/2+rc,0]) circle(rc);
            translate([dfan/2-rc,-dfan/2+rc,0]) circle(rc);
        }
        // screw holes
        translate([dfan/2-rc,dfan/2-rc,0]) circle(dfanscr/2);
        translate([-dfan/2+rc,dfan/2-rc,0]) circle(dfanscr/2);
        translate([-dfan/2+rc,-dfan/2+rc,0]) circle(dfanscr/2);
        translate([dfan/2-rc,-dfan/2+rc,0]) circle(dfanscr/2);
        // hole
        circle(d=dhole);
    }
}

module lid_mount() {
    rotate([180,tilt,0]) union() {
        linear_extrude(hlid+wt) difference() {
            circle(dlid/2+wt);
            circle(dlid/2);
        }
        linear_extrude(wt) difference() {
            circle(dlid/2+wt);
            // hole for air inlet
            translate([-offset,0,0]) circle(din/2-wt);
            // hole for air outlet
            translate([offset,0,0]) circle(dout/2-wt);
            // holes for cables
            translate([0,1.5*offset,0]) circle(d=dcable);
            translate([0,-1.5*offset,0]) circle(d=dcable);
        }
        // exhaust
        translate([2*offset,0,0]) rotate([90,0,0])
            rotate_extrude(angle=45) translate([-offset,0,0]) difference() {
                circle(d=dout);
                circle(d=dout-2*wt);
            }
        translate([offset,0,wt]) linear_extrude(hlid) {
            difference() {
                circle(d=dout);
                circle(d=dout-2*wt);
            }
        }
        //
        translate([0,1.5*offset,-hlid]) linear_extrude(20) {
            difference() {
                circle(d=dcable+2*wt);
                circle(d=dcable);
            }
        }
        translate([0,-1.5*offset,-9]) linear_extrude(20) {
            difference() {
                circle(d=dcable+2*wt);
                circle(d=dcable);
            }
        }
    }
}

module fan_tube() {
    dh=0.01;
    difference() {
        hull() {
            cylinder(d=dfan, h=dh);
            translate([0,0,-sep]) rotate([0,tilt,0])
                translate([-offset,0,0]) cylinder(d=din, h=dh);
        }
        hull() {
            cylinder(d=dfan-2*wt, h=dh);
            translate([0,0,-sep-dh]) rotate([0,tilt,0])
                translate([-offset,0,0]) cylinder(d=din-2*wt, h=dh);
        }
    }
}