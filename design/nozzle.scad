$fn=32;

dplate=30;                  // diameter of nozzle mount plate
dscr=3;                  // diameter of screw holes in fan
rc=3;                       // corner radius
wt=2;                       // wall thickness
dhole=14;

nozzle_mount(dhole=dhole);

difference() {
    rotate_extrude(angle=360) {
        polygon([[0,1.5*wt],[dhole/2+wt,1.5*wt],[20,50],[0,50]]);
    }
    rotate_extrude(angle=360) {
        polygon([[0,1.5*wt],[dhole/2,1.5*wt],[20-wt,50],[0,50]]);
    }
}

// ===================================================================================

module nozzle_mount(dhole) {
    linear_extrude(1.5*wt) difference() {
        // mounting plate for fan
        hull() {
            translate([dplate/2-rc,dplate/2-rc,0]) circle(rc);
            translate([-dplate/2+rc,dplate/2-rc,0]) circle(rc);
            translate([-dplate/2+rc,-dplate/2+rc,0]) circle(rc);
            translate([dplate/2-rc,-dplate/2+rc,0]) circle(rc);
        }
        // screw holes
        translate([dplate/2-rc,dplate/2-rc,0]) circle(dscr/2);
        translate([-dplate/2+rc,dplate/2-rc,0]) circle(dscr/2);
        translate([-dplate/2+rc,-dplate/2+rc,0]) circle(dscr/2);
        translate([dplate/2-rc,-dplate/2+rc,0]) circle(dscr/2);
        // hole
        circle(d=dhole);
    }
}