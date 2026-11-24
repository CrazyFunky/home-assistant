// ESPHome air quality sensor enclosure
// Target parts: NodeMCU v2, MH-Z19, SDS011, DHT11
// Units: millimeters

$fn = 36;

test_fit = false;

case_w = 130;
case_d = 105;
case_h = 42;
wall = 2.4;
floor_h = 2.4;
corner_r = 4;

lid_h = 16;
base_h = case_h - lid_h;

sds_w = 72;
sds_d = 72;
sds_h = 25;

nodemcu_w = 28;
nodemcu_d = 52;
nodemcu_h = 14;

mhz_w = 36;
mhz_d = 24;
mhz_h = 12;

dht_w = 18;
dht_d = 36;
slot_w = 2.4;

module_clearance = 1.5;

module_sds_x = 58;
module_sds_y = 48;

module_mhz_x = 27;
module_mhz_y = 20;

module_node_x = 93;
module_node_y = 32;

module_dht_x = 23;
module_dht_y = 87;

module rounded_box(w, d, h, r) {
  hull() {
    translate([r, r, 0]) cylinder(h = h, r = r);
    translate([w - r, r, 0]) cylinder(h = h, r = r);
    translate([r, d - r, 0]) cylinder(h = h, r = r);
    translate([w - r, d - r, 0]) cylinder(h = h, r = r);
  }
}

module hollow_base() {
  difference() {
    rounded_box(case_w, case_d, base_h, corner_r);
    translate([wall, wall, floor_h])
      rounded_box(case_w - wall * 2, case_d - wall * 2, base_h + 1, corner_r - 1);

    // Rear USB cable opening for NodeMCU.
    translate([module_node_x - 8, case_d - wall - 0.2, 8])
      cube([22, wall + 1, 13]);

    // Side cable service openings.
    translate([-0.2, 75, 10])
      cube([wall + 1, 16, 8]);
    translate([case_w - wall - 0.2, 55, 10])
      cube([wall + 1, 20, 8]);
  }
}

module lid_shell() {
  difference() {
    rounded_box(case_w, case_d, lid_h, corner_r);
    translate([wall, wall, -1])
      rounded_box(case_w - wall * 2, case_d - wall * 2, lid_h, corner_r - 1);

    // SDS011 front circular intake grid.
    for (x = [module_sds_x - 24 : 10 : module_sds_x + 24]) {
      for (y = [module_sds_y - 24 : 10 : module_sds_y + 24]) {
        if ((x - module_sds_x) * (x - module_sds_x) + (y - module_sds_y) * (y - module_sds_y) < 32 * 32)
          translate([x, y, -1]) cylinder(h = lid_h + 2, r = 2.3);
      }
    }

    // MH-Z19 side/top ventilation.
    for (i = [0 : 5]) {
      translate([module_mhz_x - 18 + i * 7, 6, 4])
        cube([slot_w, 18, lid_h]);
    }

    // DHT11 side ventilation.
    for (i = [0 : 4]) {
      translate([8, module_dht_y - 14 + i * 7, 4])
        cube([18, slot_w, lid_h]);
    }

    // Warm air exhaust slots.
    for (i = [0 : 7]) {
      translate([case_w - 58 + i * 7, case_d - 13, 4])
        cube([slot_w, 24, lid_h]);
    }
  }
}

module post(x, y, h = 8, outer = 5, inner = 2.2) {
  difference() {
    translate([x, y, floor_h])
      cylinder(h = h, r = outer / 2);
    translate([x, y, floor_h - 0.5])
      cylinder(h = h + 1, r = inner / 2);
  }
}

module cable_anchor(x, y) {
  translate([x, y, floor_h])
    difference() {
      cube([14, 5, 5], center = true);
      translate([0, 0, -0.5]) cube([8, 6, 3], center = true);
    }
}

module component_footprints() {
  // SDS011 footprint and four retention posts.
  translate([module_sds_x - sds_w / 2 - module_clearance, module_sds_y - sds_d / 2 - module_clearance, floor_h])
    cube([sds_w + module_clearance * 2, sds_d + module_clearance * 2, 1.2]);

  post(module_sds_x - 34, module_sds_y - 34, 5);
  post(module_sds_x + 34, module_sds_y - 34, 5);
  post(module_sds_x - 34, module_sds_y + 34, 5);
  post(module_sds_x + 34, module_sds_y + 34, 5);

  // NodeMCU supports.
  post(module_node_x - 14, module_node_y - 24, 6, 4.5, 1.8);
  post(module_node_x + 14, module_node_y - 24, 6, 4.5, 1.8);
  post(module_node_x - 14, module_node_y + 24, 6, 4.5, 1.8);
  post(module_node_x + 14, module_node_y + 24, 6, 4.5, 1.8);

  // MH-Z19 tray.
  translate([module_mhz_x - mhz_w / 2 - 1, module_mhz_y - mhz_d / 2 - 1, floor_h])
    difference() {
      cube([mhz_w + 2, mhz_d + 2, 4]);
      translate([2, 2, 1.2]) cube([mhz_w - 2, mhz_d - 2, 4]);
    }

  // DHT11 loose pocket. Keep it close to a vent and away from the ESP board.
  translate([module_dht_x - dht_w / 2 - 1, module_dht_y - dht_d / 2 - 1, floor_h])
    difference() {
      cube([dht_w + 2, dht_d + 2, 4]);
      translate([2, 2, 1.2]) cube([dht_w - 2, dht_d - 2, 4]);
    }

  cable_anchor(96, 74);
  cable_anchor(58, 12);
}

module base_part() {
  hollow_base();
  component_footprints();
}

module lid_part() {
  translate([0, 0, 0])
    lid_shell();

  // Inner lip for lid alignment.
  translate([wall + 0.8, wall + 0.8, 0])
    difference() {
      rounded_box(case_w - (wall + 0.8) * 2, case_d - (wall + 0.8) * 2, 5, corner_r - 1.5);
      translate([wall, wall, -1])
        rounded_box(case_w - (wall + 0.8) * 2 - wall * 2, case_d - (wall + 0.8) * 2 - wall * 2, 7, corner_r - 2);
    }
}

if (test_fit) {
  base_part();
} else {
  translate([0, 0, 0]) base_part();
  translate([0, case_d + 12, 0]) lid_part();
}
