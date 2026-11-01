---
title: "Unofficial Service Manual"
source: https://zeromanual.com/wiki/Unofficial_Service_Manual
archived: https://web.archive.org/web/20250226212908/https://zeromanual.com/wiki/Unofficial_Service_Manual
captured: 2025-02-26
last_modified: "10 July 2020 00:05"
categories: ["Service Manual", "Charger", "HV Component"]
---

# Unofficial Service Manual

## Overview

This describes the Zero motorcycle platform and includes as many service tasks not described (or incompletely described) in the [official Owner's Manuals](Official_Owners_Manual.md "Official Owners Manual") as customers have identified.

Some information might be hearsay or not completely communicated, but attempts have been made to verify as much as possible.

As with anything in a wiki environment, whatever you undertake with this as a guide is your own responsibility.

**Coverage**

- S,DS,SR,DSR *AKA* [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform)/[Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2)

  Unless otherwise stated, this manual refers to the shared [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) and the 2013+ years ([Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2)) in particular.
- FX,FXS *AKA* [XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform)/[Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2)

  Coverage is reasonable, but progress here would benefit from volunteers invested in these models.
- Pre-2013 models *AKA* [Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1)

  Maintenance coverage to keep their powertrains running (battery, controller, and motor).

  These models varied significantly by year and were produced in smaller numbers.
- SR/F *AKA* [FST Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FST_Platform)/[Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3)

  The [SRF Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SRF_Model) bikes have only just started reaching customers in small numbers, and represents a very large shift in construction and powertrain details, so this may take some time.

  See [Unofficial Manual updates based on Zero's SRF](http://electricmotorcycleforum.com/boards/index.php?topic=8758) on the EMF forum for notes gathered so far.

## Platforms

Zero motorcycles benefit from some commonality around the powertrain. The [motor](#Motor), [controller](#Controller), [BMS](#Battery_Management_System) and [MBB](#Main_Bike_Board) are more or less shared across all models, along with handlebars and controls.

### [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform)

The [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) SDS Platform follows the [Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1) [S Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/S_Platform), building on a single evolving frame design around a compartment sized for a full battery power pack (the [Monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith)), but also featuring a 3-[Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brick) battery or a [Longbrick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Longbrick) battery for lower entry-cost models.

**Models**

[S Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/S_Model)

[DS Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DS_Model)

[SR Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SR_Model)

[DSR Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DSR_Model)

**Fleet variants**

SP, DSP, SRP, DSRP - Law enforcement / patrol.

### [XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform)

The [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) XMX platform follows on the [Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1) [X Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/X_Platform) and builds on a single lighter-weight frame design around two bricks of batteries.

**Models**

[FX Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FX_Model)

[FXS Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FXS_Model)

**Fleet variants**

FXP, FXSP - Law enforcement / patrol.

[MMX Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MMX_Model) - Military built-to-order

**Older Variants**

XU ([2013](http://www.zeromotorcycles.com/zero-xu/2013/)): a low power street/training model.

MX ([2013](http://www.zeromotorcycles.com/zero-mx/2013/)): a motocross (tall suspension offroad, street homologation optional) model.

### [FST Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FST_Platform)

This is the [Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3) platform listed for the [SRF Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SRF_Model) and [SRS Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SRS_Model).

## General Information

### VIN

The [VIN](https://en.wikipedia.org/wiki/Vehicle_identification_number) is inscribed on the front head tube of the frame per the official manual.

See the [VIN guide](https://web.archive.org/web/2025/https://zeromanual.com/wiki/VIN_Guide) to understand how the VIN describes your vehicle, as compiled across manual revisions.

### Systems

This is a very simplified way of looking at the bike’s systems functions and general purposes, linking to relevant sections.

#### Mechanical Systems

- [Frame](#Frame)
- [Steering](#Steering)
- [Suspension](#Suspension)
- [Wheels](#Wheels)
- [Final Drive](#Final_Drive)
- [Brakes](#Brakes)

#### Powertrain Systems

- [Throttle](#Throttle)
- [MBB](#Main_Bike_Board)
- [Controller](#Controller)
- [Motor](#Motor)

#### Energy Systems

- [Battery](#Battery)
  - [BMS](#Battery_Management_System)
  - [Contactor](#Contactor)
- [CCU](#Charging_Control_Unit)
- [Charger](#Charger)

#### Electrical Systems

- [DC-DC 12V Converter](#DC-DC_12V_converter)
- [Fuse Block](#Fuse_Block)

## General Maintenance

Mostly, refer to the [official owners' manual](Official_Owners_Manual.md "Official Owners Manual") for regular and general maintenance.

### [Lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift)

Some maintenance tasks are better performed with the wheels off the ground.

The armored pan under the battery that protects onboard charging units is strong enough and positioned well to use a center lift.

**Recommendation**

![Center lift under S model belly pan](../images/Onlift.jpeg) *Center lift under S model belly pan*

![FXS from below.](../images/Fxs_view_from_below.jpg) *FXS from below.*

Using a scissor lift center stand is an easy method to lift the bike.

[Rage Powersports BW-1604A](http://www.ragepowersports.com/motorcycle-products/black-widow-center-jack-and-dolly/) has been spotted at Zero HQ, but other manufacturers make very equivalent stands.

A center lift is easier than a rear stand to operate solo, and it is more compact than the rear stand although much heavier.

**Location (S Platform)**

Use a center lift under the battery compartment.

- Orient the center stand so that it runs side-to-side to provide lateral stability.
- Place it under the *rear* of the battery compartment to lift the bike's front and rear equally.
- Place it under the *front* of the battery compartment to lift the bike's front and leave the rear tire in floor contact.
- Strap the bike securely (through the center frame tube, say) to avoid toppling it.

**Confirmed fits**

- [Drag Specialties Center Jack](http://www.dragspecialties.com/products/?productId=121879) (all models) uses a 15/16 hex wrench to raise and lower the lift.
- [Generic Lift](https://www.amazon.com/gp/product/B0196PAZ1S/ref=oh_aui_search_detailpage?ie=UTF8&psc=1) uses a 7/8 hex wrench/socket; should work for all models, confirmed for 2014 SR.

**Location (X Platform)**

The FXS (at least) has three bolts sticking out from the pan under the bike.

- Orient the center stand so that it runs side-to-side to provide lateral stability.
- You can put a rubber pad on your lift to make it easier to use it over the bolts.

**Confirmed fits**

- [MSR Pro Lift Stand](http://www.motorcycle-superstore.com/28665/i/msr-pro-lift-stand) for the FX, but not other models (even FXS) because of height issues.

**References**

- [Discussion thread](http://electricmotorcycleforum.com/boards/index.php?topic=6589)
- [Video of DSR lifted by scissor jack.](https://www.youtube.com/watch?v=6wrPLi9Yags)
- [Rage Powersports BW-1604A scissor jack unboxing](https://www.youtube.com/watch?v=TnqBsha33bs) by [E Shattow on YouTube]:

### [Front Stand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Stand)

**When To Use**

A front stand is the easiest way to:

- Perform [Front Wheel Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Wheel_Removal).
- Remove and replace the [Belly Pan](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belly_Pan).

**Spool Stands**

- The Zero does not offer axle attachment points for spools for a front stand.

**Steering Head Pin Stands**

- 2014+ models(?) have a steering pin diameter of 5/8".
- 2012-2013 Zero models have an 8mm diameter (from a 2013 Zero S report and some checking around), with no vendor match.
- The DS/DSR/FX models' high front fender must be removed (or drilled through) to use a pin for the front steering head.

**Confirmed fits**

- Pit Bull offers [Pin #7, Front](https://www.pit-bull.com/pin-7-front-f0001-007) to fit the 5/8" steering pin diameter.
- [Pit Bull Hybrid Dual Lift Stand Zero S/SR/DS/FX (Order should automatically include pin #7)](https://www.revzilla.com/motorcycle/pit-bull-hybrid-dual-lift-stand-zero-s-sr-ds-fx).

  Verify your steering stem before ordering.

  [Front Stand Chart](https://www.revzilla.com/assets/0001/8394/20150516_FL-Pitbull_Front_Stand_Chart_1_NON_BRANDED.pdf).

| Years | Platform | Front Pin | Rear Pin | Rear Supports | Restraint |
| --- | --- | --- | --- | --- | --- |
| 2013 | S & X | None! (8mm ⌀) | [Pin Fitting Only - Zero Motorcycles (Axle: 23-04736)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-pin-fitting-only-zero-motorcycles-axle-23-74036-f0075nf-001) | [Top Supports (Pair), Standard Rear Stand](https://www.pit-bull.com/zero-motorcycles/top-supports-pair-standard-rear-stand-f0002-001) <br> [Top Supports (Pair), SS Rear Stand](https://www.pit-bull.com/zero-motorcycles/top-supports-pair-ss-rear-stand-f0028-001) | [Trailer Restraint System - Zero Motorcycles (Axle: 23-04736)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-system-zero-motorcycles-axle-2304736-f0075nf-000) |
| 2014 | 〃 | [Pin #7, Front](https://www.pit-bull.com/pin-7-front-f0001-007) | 〃 | 〃 | 〃 |
| 2015+ | 〃 | 〃 | [Pin Fitting Only - Zero Motorcycles (Axle: 23-08032)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-pin-fitting-only-zero-motorcycles-axle-2308032-f0075kj-001) | 〃 | [Trailer Restraint System - Zero Motorcycles (Axle: 23-08032)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-system-zero-motorcycles-axle-2308032-f0075kj-000) |

### [Rear Stand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Stand)

**Inexpensive Jack Stands and a 2x4**

- Will Burk shared his technique [Cheap and Easy Motorcycle Lift](https://www.youtube.com/watch?v=_iBNLDCyRbs) for raising the rear wheel off the ground with a pair of jack stands and a 2x4:

**Swingarm attachment**

The Zero does not offer [swingarm](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Swingarm) attachment points for spools for a rear stand.

A rear stand can work if it cradles the underside of the swingarm snugly.

This can work but takes a little care to operate single-handedly.

**Confirmed fits**

- [Pit Bull Standard Rear Stand](https://www.revzilla.com/motorcycle/pit-bull-standard-rear-stand)
- [Pit Bull Forward Handle Standard Rear Stand](https://www.revzilla.com/motorcycle/pit-bull-forward-handle-standard-rear-stand)
- [Haul-Master 1000 Lb. Capacity Motorcycle Swingarm Rear Stand (Harbor Freight)](https://www.harborfreight.com/motorcycle-swingarm-rear-stand-65620.html)

**Axle Attachment**

Custom Fabrication

An axle stand can be fabricated, like this [Home made rear axle stand on Zero FXS](http://electricmotorcycleforum.com/boards/index.php?topic=6985).

| Years | Platform | Front Pin | Rear Pin | Rear Supports | Restraint |
| --- | --- | --- | --- | --- | --- |
| 2013 | S & X | None! (8mm ⌀) | [Pin Fitting Only - Zero Motorcycles (Axle: 23-04736)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-pin-fitting-only-zero-motorcycles-axle-23-74036-f0075nf-001) | [Top Supports (Pair), Standard Rear Stand](https://www.pit-bull.com/zero-motorcycles/top-supports-pair-standard-rear-stand-f0002-001) <br> [Top Supports (Pair), SS Rear Stand](https://www.pit-bull.com/zero-motorcycles/top-supports-pair-ss-rear-stand-f0028-001) | [Trailer Restraint System - Zero Motorcycles (Axle: 23-04736)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-system-zero-motorcycles-axle-2304736-f0075nf-000) |
| 2014 | 〃 | [Pin #7, Front](https://www.pit-bull.com/pin-7-front-f0001-007) | 〃 | 〃 | 〃 |
| 2015+ | 〃 | 〃 | [Pin Fitting Only - Zero Motorcycles (Axle: 23-08032)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-pin-fitting-only-zero-motorcycles-axle-2308032-f0075kj-001) | 〃 | [Trailer Restraint System - Zero Motorcycles (Axle: 23-08032)](https://www.pit-bull.com/zero-motorcycles/trailer-restraint-system-zero-motorcycles-axle-2308032-f0075kj-000) |

### Tools

See the separate [Tool Kits](Tool_Kits.md "Tool Kits") article for a curated short list of tools with their purposes.

NOTE: integrate or meld notes below with that article.

[Tools and parts to support your bike](http://electricmotorcycleforum.com/boards/index.php?topic=5878)

A travel kit for a motorcycle is always a good idea, but Zero doesn't include a default set. They do sell a [tool kit](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_4&products_id=128) which covers many common tasks.

**Tools for Everyday Riding**

- Torx T45 for MY2015+ to remove the [seat](#Seat) for [fuse block](#Fuse_Block) access.
- 3mm allen key for [tank plastics](#Tank_Plastics) and [headlamp](#Headlamp) upper mount screws.
- 4mm allen key for [headlamp](#Headlamp) lower mount screws.
- 5mm allen key for the [front brake lever](#Front_Brake_Lever) and front wheel pinch bolt.
- Tire pressure gauge.
- 10mm, 13mm wrench (or monkey wrench) for [belt tension adjustment](#Belt_Tension_Adjustment) and front brake calipers.

### [Consumables](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Consumables)

These collect useful spare parts for [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) models.

**Spare Parts for Everyday Riding**

- 12V fuses (10A, 15A typically).
- Tire patch kit, suitable for tubed (pre-2015 DS or FX bikes) or tubeless tires (all others).
- Cable ties and electrical tape for wiring.

**Spare Parts for Travel**

- [Belt](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt)

  ~$90, only available from Zero.

  Expect to eventually use it as replacement; avoids a delay waiting on delivery.

  Tools for [belt replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Drive_Belt_Replacement_Procedure): 27mm socket with breaker bar, 10mm hex key...
- [Eaton JJN-100 fuse](http://www.mouser.com/ProductDetail/Bussmann-Eaton/JJN-100/?qs=vco6xy%252beH1pHxfCrJKaBAA%3D%3D) or size-matched 200V-rated fuses (30A will do in a pinch, being lower-spec)

  Fixes the [accessory charging circuit](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) which can be circumstantially blown without compromising the main boards.

### [Pre-Ride Checklist](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Pre-Ride_Checklist)

|  | Item | What to Check | Look For | Check Off |
| --- | --- | --- | --- | --- |
| Tires And Wheels | Tires | Condition | Tread depth, wear, weathering, evenly seated, bulges, embedded objects. | [Front](#Front_Wheel) & [Rear](#Rear_Wheel) |
| 〃 | 〃 | Air Pressure | Check When Cold; Adjust to Load | 〃 |
| 〃 | Wheels | Spokes | Bent/broken/missing. Check tension at top of wheel: "ring" is okay, "thud" means loose. | 〃 |
| 〃 | 〃 | Cast | Cracks or dents | 〃 |
| 〃 | 〃 | Rims | Out of round by more than 5mm. Spin the wheel against a stationary pointer | 〃 |
| 〃 | 〃 | Bearings | Grab the tire and flex it; no freeplay (click) between the hub and axle; no growl or squeak when spinning. | 〃 |
| 〃 | 〃 | Seals | Cracked or torn, no grease | 〃 |
| 〃 | [Brakes](#Brakes) | Function | Each brake alone can hold the bike stationary | 〃 |
| 〃 | 〃 | Condition | Worn [pads](#Brake_Pads) or discs | 〃 |
| Controls | [Handlebars](#Handlebars) | Condition | Bars are straight, turn freely, handgrips and bar ends are secure. |  |
| 〃 | [Brake Lever](#Brake_Lever) / [Brake Pedal](#Rear_Brake_Actuator) | Condition | Not broken/bent/cracked; adjusted properly. |  |
| 〃 | 〃 | Pivots | Lubricated |  |
| 〃 | Brake Hoses | Condition | No cuts/cracks/leaks/bulges/chafing/deterioration. |  |
| 〃 | 〃 | Routing | No interference or pull at the steering head; no sharp angles; support clamps in place. |  |
| 〃 | [Throttle](#Throttle) | Operation | Moves freely; snaps closed. |  |
| Lights & Electrics | [Headlamp](#Headlamp)/[Running light](#Running_Light) | Condition | Turns on; no cracks; mounted securely; clean reflector. |  |
| 〃 | 〃 | Aim | Just below horizontal and not skewed left or right. |  |
| 〃 | [Tail Lights](#Tail_Light) | Condition | No cracks; clean and bright. |  |
| 〃 | 〃 | Operation | Running light always on; brighter with front or rear brake pressed. |  |
| 〃 | Switches | Operation | All switches function correctly: motor cut-out, hi/low beam, turn signal, hazard switch. |  |
| 〃 | [Turn signals](#Turn_Signals) | Operation | No cracks; flashes with left and right turn signal switch usage; resets per switch. |  |
| 〃 | [Mirrors](#Mirrors) | Condition | No cracks; clean, mount and swivel joints are tight |  |
| 〃 | 〃 | Aim | Check/adjust while seated on the bike off the kickstand. |  |
| 〃 | Wiring | Condition | No fraying or chafing; insulated. |  |
| 〃 | 〃 | Routing | No pinching, interference, or pulling at the steering head or suspension; wire looms and ties in place; connectors tight and clean. |  |
| Oil & Fluids | Hydraulic Fluid | Level | Check front and rear reservoirs |  |
| 〃 | 〃 | Cleanliness | Check whether the fluid is very dark, foamed, or has water |  |
| Chassis | [Frame](#Frame) | Condition | No cracks at gussets or accessory mounts; no paint lifting |  |
| 〃 | 〃 | [Steering-Head Bearings](#Steering_Head_Bearing) | No detent or tight spots through full travel; raise front wheel and check for play by pulling/pushing forks. |  |
| 〃 | 〃 | [Swingarm](#Swingarm) Bushings | Raise the rear wheel and check for play by pulling/pushing swingarm. |  |
| 〃 | Suspension | [Front Forks](#Front_Forks) | Smooth travel, equal air pressure/damping, anti-dive settings. | Left & Right |
| 〃 | 〃 | [Rear Shock](#Rear_Shock) | Smooth travel, equal pre-load/air pressure/damping settings, linkage moves freely and is lubricated. |  |
| 〃 | [Belt](#Belt) | [Tension](#Belt_Tension_Check) | Check at tightest point |  |
| 〃 | 〃 | [Alignment](#Belt_Tension_Check) | Check position on rear sprocket; spin the wheel to check changing position |  |
| 〃 | 〃 | [Sprockets](#Sprocket) | Teeth not hooked or chipped; clean and securely mounted |  |
| 〃 | Fasteners | Threaded | Tight; none missing; check for corrosion |  |
| 〃 | 〃 | Clips and Pins | None broken or missing |  |
| Stands | [Side Stand](#Kickstand) | Condition | No cracks; not bent; cutout switch equipped and working |  |
| 〃 | 〃 | Retention | Springs into place; tension holds position up or down |  |

### [Fastener Maintenance](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Fastener_Maintenance)

To maintain the fasteners (bolts and screws), always check for loose or corroding bolts.

**Torque**

- For torques, see [Fastener Specifications](Fastener_Specifications.md "Fastener Specifications"), which gathers all the officially recommended torque and other settings for various fasteners.

**Locking**

- Use blue Loctite threadlocker for non-conductive bolts.

**Corrosion**

TODO: recommend a corrosion inhibitor.

## Frame/Bodywork

### Frame

#### [S Platform Frame](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Frame)

| | |
| --- | --- |
| ![2013 S Platform Frame](../images/2013_zero-s_detail_frame_978x385_feature_8082_cropped.png) *2013 S Platform Frame* | ![2014-2016 S Platform Frame](../images/2016_zero-s_detail_frame_978x385_feature_15456_cropped.png) *2014-2016 S Platform Frame* |
| ![2014S frame isometric](../images/2014-zero-S-frame-iso.png) *2014S frame isometric* |  |

The 2013+ Zero frame for S/DS/SR/DSR bikes is made of anodized aluminum, weighs 23lbs, and is a combination of cast parts and welded square tubing of 1-inch outer width.

The frame slips onto the battery pack case over the top and attaches to it with four major bolts around the bottom. The charger is attached to the underside with a protective plate covering it (plastic for S/SR, aluminum for DS/DSR).

**Attachment Points**

The frame offers a number of rivet nut attachment points for the lower plastics.

The rivet nuts are sized to accept M5 bolts (a total depth of 20mm is available without marring the inside of the frame bar) with a 6mm shoulder to a depth of 5mm. (A longer shoulder and length are required for fastening a bracket beyond that.)

From 2015 onwards, the frame has extra attachment points made for the crash bars used for fleet/police models.

Two extra rivet nut holes on each side of the frame diagonal shoulder of the same size. They are 30mm apart (center to center).

The lower bash plate has similar modifications from that year - two rivet nut holes pre-made for M6 bolts and capped by threaded plastic inserts on each side for the lower mount. There is perhaps 10mm thread depth or allowance between the outer surface of the plate and the onboard charger enclosure.

On prior year models, the OEM or dealer would make these fittings.

**Vertical Stanchions**

- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Right_Front.png)

  Vertical Stanchion Right
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Right_Inside.png)

  Vertical Stanchion Right
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Right_Rear.png)

  Vertical Stanchion Right
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Left_Inside_Lower.png)

  Vertical Stanchion Left
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Left_Inside_Plug_1.png)

  Vertical Stanchion Left
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Left_Inside_Plug_2.png)

  Vertical Stanchion Left
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Left_Inside_Plug_3.png)

  Vertical Stanchion Left
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Left_Inside.png)

  Vertical Stanchion Left
- ![](../images/2017-S-Frame_-_Vertical_Stanchion_Left_Outside.png)

  Vertical Stanchion Left

**Tail Horns**

- ![](../images/2017-S-Frame_-_Tail_Horns_Side.png)

  Tail Horns (Left)
- ![](../images/2017-S-Frame_-_Tail_Horns_Top.png)

  Tail Horns (Top)
- ![](../images/2017-S-Frame_-_Horns_Rear.png)

  Tail Horns (Rear)

**Neck and Shoulder**

- ![](../images/2017-S-Frame_-_Neck_Above.png)

  Neck and Shoulder (Top)
- ![](../images/2017-S-Frame_-_Neck_Rear.png)

  Neck and Shoulder (Rear)
- ![](../images/2017-S-Frame_-_Shoulder_Reinforcement.png)

  Neck and Shoulder
- ![](../images/2017-S-Frame_-_Left_Shoulder_Mount_Holes.png)

  Neck and Shoulder (Left)

**Battery Carrier Tray**

- ![](../images/2017-S-Frame_-_Battery_Carrier_Tray_Top.png)

  Battery Carrier Tray
- ![](../images/2017-S-Frame_-_Battery_Carrier_Tray_Forward_Left_Holes.png)

  Battery Carrier Tray (Left Holes)
- ![](../images/2017-S-Frame_-_Battery_Carrier_Tray_Forward_Right_Holes.png)

  Battery Carrier Tray (Right Holes)
- ![](../images/2017-S-Frame_-_Battery_Carrier_Tray_Rear.png)

  Battery Carrier Tray (Rear)

**Board Mounting Plate**

- ![](../images/2017-S-Frame_-_Board_Mounting_Plate_Left_Bracket.png)

  Board Mounting Bracket (Left)
- ![](../images/2017-S-Frame_-_Board_Mounting_Plate_Right_Bracket.png)

  Board Mounting Bracket (Right)

##### [Frame Tube](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Frame_Tube)

![2018 SR Frame Tube Inner view](../images/2018-zero-sr-frame-tube.JPG) *2018 SR Frame Tube Inner view*

The frame has a tube running through the center of the bike where the tail horns meet the vertical stanchions and the main forward frame beams.

The tube functions as the anchor and hinge support for the rear shock.

For 2012-2014 models, this inner tube functions effectively as storage for the [Charger Power Cord](#Charger_Power_Cord).

2015+ models have a brace in the center of the hole which reduces the diameter in that section.

The rough edges on this brace can abrade the power cord, so for these models, storing the cord there can wear it out over time.

| | |
| --- | --- |
| Inner diameter (2015+) | ~58mm |
| Center Brace minimum diameter (2015+) | ~40mm |

**References**

[Re: Through-frame security aperture size?](http://electricmotorcycleforum.com/boards/index.php?topic=8163.msg68842#msg68842)

##### [Belly Pan](https://web.archive.org/web/2025/https://zeromanual.com/wiki/S_Platform/Belly_Pan)

The Belly Pan AKA Skid Plate covers the [onboard charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) and is metallic on the DS/DSR and a very hard ABS plastic on the S/SR models.

![DS Belly Pan / Skid Plate](../images/2016-ds-skid-plate.png) *DS Belly Pan / Skid Plate*

Both variants are sturdy enough to support the bike on a centerlift.

**Parts**

S/SR: Hard plastic, part 24-07746.

DS/DSR: Aluminum alloy [5052-H32](http://asm.matweb.com/search/SpecificMaterial.asp?bassnum=ma5052h32), part 26-08051 (was 20-05126).

**Dimensions**

- Lengths
  - 20.5in from forward bevel lip to trailing edge below the motor.
  - 14.5in along the flat base.
  - 2.25in along forward bevel.
- Widths
  - 10.25in at the vertical outside face.
  - 11 15/16in edge to edge of the flange facing the frame.
- Heights
  - 2.5in from frame-facing edge to the bottom edge (not counting louver overhang).
  - 1in height 45° bevel.
- Thickness
  - 3mm for the DS/DSR metallic pan.

**Drop bar Mounts**

- 2× holes per side for M6 bolts, 45mm center-to-center forward to aft.

**Mounting**

Fastened by 8 M5×16-8.8 button head bolts, 4 per side.

Forward corner bolts fasten into corner brackets (part 20-05307) that extend the lower frame square tubing.

**[Belly Pan Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belly_Pan_Removal)**

**Video Guide**

[How to Remove the Zero's Onboard Charger by NewZeroLand on YouTube](https://www.youtube.com/watch?v=DFHQgTOMxO8) from the beginning to 2 minutes in shows very clearly how to remove the pan from a Zero SR.

**Tools**

- 3mm Allen key.

**Steps**

1. (Optional) Place the bike upright on a [front wheel stand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) if a vertical drop of the pan is suitable.
2. Loosen each of the 8 bolts retaining the belly pan (4 per side), without removing.
3. Remove each fastener in some suitable rotation so the pan isn't temporarily left dangling by one fastener.

   The pan is lightweight and can be manually suspended if convenient, or use a lift to catch the pan and lower it.
4. Set the bolts aside with the pan for replacement later.

##### [Y-Shaped Underseat Frame](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Subframe)

![2016 DSR underseat view](../images/Dsr-under-seat.JPG) *2016 DSR underseat view*

This frame piece spans the top of the frame between the part that sits behind the battery doghouse and the tail.

**Functions**

- Support and anchor the [seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Seat) by two pins extending from the forward center section.
- Anchor the rear of the [tank plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Plastics).
- Mount the [12V Fuse Block](https://web.archive.org/web/2025/https://zeromanual.com/wiki/12V_Fuse_Block) on the left rear leg.
- Distributes the seat loading between the forward frame bracket arching over the monolith, and the horns of the rear tail.

  This protects underlying cabling, as well as dampens any load on the frame that would flex the tail relative to the forward part of the frame.
- Removable (vs being frame-integrated or welded) for servicing everything above the motor (MBB, DC-DC converter, and cabling and wiring).

**Mounting**

- **Forward:** 2x 10mm hex nylon locknuts, with washers.
- **Rear:** 2x M5 socket cap bolts, 20mm length with a 2mm shoulder, 1mm depth, 6mm outer diameter, with washers.

**[Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Frame_Removal)**

**Tools**

- 10mm hex socket wrench with at least 20mm of depth.
- 5mm Allen key.

**Steps**

1. [Remove the seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Seat_Removal).
2. Use the 10mm socket wrench to loosen the locknuts anchoring the forward end of the washers.
3. Use the 5mm Allen key to loosen the bolts at each of the rear ends of the frame piece.
4. Remove the locknuts and the bolts in a coordinated pattern to avoid putting it under asymmetrical loading.
   - Take care not to lose the washers in the frame piece or in the bike's cabling areas underneath as each bolt and nut comes off.

**Installation**

1. Ensure the underlying cabling is placed in its original orientation to avoid strain.
2. Press the frame piece's fastener holes onto the corresponding threaded bolts on the frame arch over the rear of the battery.
3. Align the rear ends of the frame piece with the corresponding frame holes, and thread the bolts with washers gently into position (without tightening) to secure the frame piece.
4. Thread (without tightening) the front locknuts with washers onto the forward bolts.
5. Tighten the two forward nuts and rear bolts in a coordinated pattern to settle the frame piece into the right load-bearing orientation.
   - Take care while tightening not to strain any cables or wiring underneath the frame piece.

##### [Board Mounting Plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate)

![Front](../images/Board_Mounting_Plate_-_Front.png) *Front*

![Rear](../images/Board_Mounting_Plate_-_Rear.png) *Rear*

A vertical plate aft of the battery supports both the [Main Bike Board](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) and the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter).

The plate varies between pre-2015 model years and the following model years, likely because of the DC converter upgrade in 2015 from 300W to 500W to support ABS braking equipment power requirements.

**Attachments**

- The [Main Bike Board](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) is mounted to the rear face of the plate for 2013-2014 models, and to the rear face of the upper edge of the plate on 2015+ models.
- The [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) is mounted to the forward face of the plate for 2013-2014 models, and to the lower rear face of the plate on 2015+ models.
- The [Accessory Charging Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Accessory_Charging_Port) is screwed to a flange at the bottom of the plate via two small M2.5 allen key bolts.
- The rubber boot covering the Accessory Charging Port is attached to the flange via plastic push-rivet.
- One cable run is zip-tied to a slot in the lower left corner of the plate, accessible under the frame arms forward of the onboard charging plug.
- Another cable run is zip-tied a slot in the lower edge of the plate closer to the right side, accessible under the frame arms behind the battery.

**Mounting**

- The bracket has side flanges that affix the plate to the left and right sides of the frame.
- The top two corners of the flanges bend to the rear of the bike at a 45 degree angle, which mate to similarly-positioned flanges on the frame sides. The frame side flanges are above the plate flanges, which means when installing and removing the plate, the top must be angled towards the rear of the bike.
- The bottom two corners of the flanges bend to the rear of the bike at a 90 degree angle. The bolts which affix these corners point upwards (cap head points down).
- Fasteners
  - 4x M4 socket cap bolts, 12mm length, 0.75mm? depth, 5mm outer diameter, with washers.
  - 2x M2.5 socket cap bolts, 25mm length with a 6mm shoulder, 0.5mm? depth, 2.5mm outer diameter, with washers.
  - 2x M3 socket cap bolts, 10mm length, 0.75mm? depth, 4mm outer diameter, with washers.

**[Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Board_Mounting_Plate_Removal)**

**Tools**

- 2.5mm, 3mm, 4mm Allen keys.
- Low clearance (under 20mm) 3mm Allen key.

**Steps**

1. [Remove the seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Seat_Removal).
2. [Remove the underseat Y-shaped frame piece](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Y-Shaped_Underseat_Frame_Removal).
3. Detach the MBB by removing the two bolts holding it to the plate with a low-clearance 3mm Allen key.
   - The right side bolt will be extremely difficult to manipulate given the cables routed very close to it; consider displacing them.
4. Push the MBB aside to the left without unplugging its connectors.
5. Remove the two bolts attaching the upper left and right corners, facing 45 degrees up/forward, with a 2.5mm(?) Allen key.
6. Remove the two bolts attaching the lower left and right corners.
   - Reach them from below the frame arms on each side of the bike, just forward of the stanchions.
   - Use a 2.5mm(?) Allen key (preferably a ratcheting socket).

   | | | | |
   | --- | --- | --- | --- |
   | ![Lower edge cables](../images/Board_Mounting_Plate_-_Lower_Edge_Cables.png) *Lower edge cables* | ![Lower right bolt](../images/Board_Mounting_Plate_-_Lower_Right_Bolt.png) *Lower right bolt* | ![Lower right clip](../images/Board_Mounting_Plate_-_Lower_Right_Clip_2.png) *Lower right clip* | ![Lower right clip](../images/Board_Mounting_Plate_-_Lower_Right_Clip.png) *Lower right clip* |
7. Snip the cable run zip tie on the lower left corner of the plate.
8. Snip the cable run zip tie on the lower edge of the plate from the right side.
   - A long, narrow-bladed screwdriver can be suitable.
9. Detach the [Accessory Charging Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) from the lower flange of the plate using a 2.5mm(?) Allen key on the two narrow bolts through the plug's body holes.
10. Along the lower rear-facing edge bracket flange, push the cross-frame cable run off of the bracket.

    | | |
    | --- | --- |
    | ![Board Plate Mounting Bracket (Left)](../images/2017-S-Frame_-_Board_Mounting_Plate_Left_Bracket.png) *Board Plate Mounting Bracket (Left)* | ![Board Plate Mounting Bracket (Right)](../images/2017-S-Frame_-_Board_Mounting_Plate_Right_Bracket.png) *Board Plate Mounting Bracket (Right)* |
11. Pull the top edge of the plate to the rear of the bike so that the top mounting flange's corners clear the mating flanges on the frame.
12. *Gently* pull the plate by the DC-DC converter up and aft, minding any cabling that can get snagged on the plate to avoid straining any wires.
    - It seems easiest to pull the left side of the plate up first, to avoid clearance issues around the hydraulic lines running along the right side towards the rear brake system.

**Installation**

- (Still working on this; essentially reversing the removal but considering the various fitment dependencies ahead of time to avoid trouble).

#### [X Platform Frame](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Frame)

| | |
| --- | --- |
| ![2013 X Platform Frame](../images/2013_zero-fx_detail_frame_978x355_feature_8084_cropped.png) *2013 X Platform Frame* | ![2014-2016 X Platform Frame](../images/2016_zero-fx_detail_frame_978x355_feature_15458_cropped.png) *2014-2016 X Platform Frame* |

## Overview

The 2013+ Zero frame for FX/FXS (and X/MX/XU) bikes is made of anodized aluminum, weighs 20lbs, and is a combination of cast parts and welded square tubing of 1-inch outer width.

The frame fits two [power pack modules](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module), one [Long Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Long_Brick) module (2017), or one module and an empty space for carrying small cargo.

The FXP fleet model has a crash guard mount option like the SP/DSP models but is smaller and mounted lower.

## Paint matching

All models have the same anodized aluminum with a black finish/paint.

Some paint repair suggestions on this thread are worth examining: [FX frame touch up](http://electricmotorcycleforum.com/boards/index.php?topic=6276)

## Iterations by Year

Each year's frame from 2013 onward is incrementally improved and stronger than the prior year.

The 2014 frame changed up the way the side plastics bolt on and provides for the power tank via the carrier bracket.

The 2015 frame included pre-drilled holes for the crash guards for fleet/police models.

The 2016 frame seems to be a little more built-up and has additional members bracing the diagonals to the main beams behind the shoulder.

## Dimensions

| | |
| --- | --- |
| Width | 10in |
| Tube Width | 1in |
| Weight | ~20lb |

## Common Frame Components

The [Swingarm](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Swingarm) is at least superficially the same as on S Platform models for the same year/generation.

The [Steering head tube](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Steering_Head) seems to be the same as on S Platform models for the same year/generation.

Frontend geometry for FX may match DS/DSR, and FXS may match S/SR.

### Tail Subassembly

#### [S Platform Tail Subassembly](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tail_Subassembly)

On the SDS Platform models, there is a separate aluminum assembly supporting the tail plastics, tail extension for the license plate, and the top rack accessory that bolts into the "horns" at the aft end of the frame just after the Sevcon controller.

![Zero S tail subframe with upper plastics removed](../images/2015-zero-s-tail-subframe-uncovered.png) *Zero S tail subframe with upper plastics removed*

#### [X Platform Tail Subassembly](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Tail_Subassembly)

The X Platform tail is entirely of plastic.

The top rack accessory only connects to the tail subframe, implying a lower dynamic loading limit than for SDS platform models.

### Tail Extension

#### [S Platform Tail Extension](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tail_Extension)

The SDS Platform tail extension supports the license plate, turn signals, and reflectors at a distance from the underside of the tail.

**Construction**

The extension is made of two cast aluminum pieces, upper and lower, that fasten together.

**Wiring**

12V wiring runs through holes in the bracket's bolted mounting to the underside of the tail to each turn signal.

The barrel connector pins for the turn signals are part of the [wiring inside the tail](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tail_Wiring) behind the seat.

12V wiring runs through the extension to the license plate support bracket to power a low level illuminator bulb.

**Mounting**

The tail extension bolts into the tail subframe using a pattern of 4 M5×15 bolts with washers.

The bolts fasten upwards into the tail subframe; use a 4mm Allen key wrench to remove or replace.

**[License Plate Bulb](https://web.archive.org/web/2025/https://zeromanual.com/wiki/License_Plate_Bulb)**

This bulb illuminates the license plate as required by law enforcement agencies.

It appears to be common across all Zero models and platforms, but do confirm and correct as needed.

**Specification**

This appears to be a T3.25 Wedge 12v (4-5w) bulb.

See [2016 Zero DS(R)/S(R) License Plate Light Bulb Spec. Info Requested](https://www.electricmotorcycleforum.com/boards/index.php?topic=9356)

#### [X Platform Tail Extension](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Tail_Extension)

The XMX Platform tail extension supports the license plate, turn signals, and reflectors from the underside of the tail.

The extension runs along the inside/underside of the tail plastics.

**Construction**

The extension is made of two cast aluminum pieces, upper and lower, that fasten together.

**Wiring**

12V wiring runs through holes in the bracket's bolted mounting to the underside of the tail to each turn signal.

The barrel connector pins for the turn signals are part of the [wiring inside the tail](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Tail_Wiring) behind the seat.

12V wiring runs through the extension to the license plate support bracket to power a low level illuminator bulb.

### [Kickstand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand)

Zero's models' kickstands are made from cast aluminum and swings outward from the left side.

There is a safety interlock Hall sensor [switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Switch) at the pivot that prevents the motor from operating when the kickstand is down.

| Years | Model | Length | Part no |
| --- | --- | --- | --- |
| 2013-2014? | S/SR | shorter than the DS/DSR | 20-05660 03 |
| 〃 | DS/DSR | 10.8" / 275mm | 20-05661 03 |
| 〃 | FX | 15.0" / 380mm | 20-05662 03 |
| 〃 | FXS |  |  |
| 2015+ | FX | 13.5" / 343mm |  |
| 〃 | FXS | 11.8" / 300mm |  |

Both DS and FX kickstands are identical from the spring screw up to the pivot, and should interchange.

All the 2013+ kickstands uses the same pivot pin & spring.

**References**

[Re: 2016 FXS Lowered Ride Height OEM Shock, Dual Use Tires, Drop Bars, Hand Guards,](http://electricmotorcycleforum.com/boards/index.php?topic=6640.msg53545#msg53545)

[Help needed: Kickstand "bent"](http://electricmotorcycleforum.com/boards/index.php?topic=6800.msg54953#msg54953)

**Mounting**

[3/8" E clip, Zero part no 90-0283700](http://electricmotorcycleforum.com/boards/index.php?topic=6800.msg55011#msg55011), also available generically.

[Clevis pin custom, Zero part no 90-0279900](http://electricmotorcycleforum.com/boards/index.php?topic=6800.msg55011#msg55011).

Mounting bracket, custom

**Maintenance**

The official manual recommends keeping the pivot greased as necessary with a six-month check interval.

**Problems**

A [Loose Kickstand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loose_Kickstand) can result from inadequate greasing over time.

**[Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Replacement)**

This replaces the [Kickstand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand).

See [Kickstand Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Removal) and [Kickstand Install](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Install) for now.

**[Install](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Install)**

**Tools**

- [Center lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) or stand.
- Large flat-blade screwdriver or specialized tool like [drum brake spring pliers](https://www.google.com/search?q=drum+brake+spring+pliers) for spring removal and replacement.
- E-clip tool (or needlenose pliers) for the 3/8" E-clip.

**Steps**

1. *(When replacing)* Remove the allen bolt securing the springs to the old kickstand.
2. *(When replacing)* Transfer the 2 bronze bushings from the old kickstand:
   1. Remove the 2 bronze bushings from the old kickstand.
   2. Clean and grease bushings.
   3. Insert bushings into new kickstand and replace chamfered bolt with springs.

      My chamfered bolt was not very tight and I assume it was being held in from the spring tension.

      I went to tighten it all the way in but that seemed to push the springs out too far.

      I put blue Loctite on it and threaded it about half way in.

      I will check this after a few rides to ensure it does not fall out!
3. Place the new kickstand onto the pivot.
4. Install the pin and spring

   **Pin Before Spring**

   1. Insert the pin.
   2. Raise the kickstand to its stowed/horizontal position.

      This minimizes the amount of force/extension to install the new spring.
   3. Install the spring over the kickstand hook with a suitable tool (see tools requirements).

   **Spring before pin**

   Have the pin and a tapered punch that fits nicely in the hole ready to go.

   1. Clean the pin and apply fresh grease to it.
   2. Hook the springs onto the frame, grip the kickstand with both hands, put your shoulder into the bike so it won’t tip.
   3. While pushing straight down on the kickstand, get it onto the frame and insert the tapered punch.
   4. Now raise the kickstand into the stowed/horizontal position.
   5. Remove punch.

      The hole will be almost aligned.
   6. Insert the pin as far as it will go, mine stopped at the frame.
   7. With the kickstand still in the up position, tap the bottom of the kickstand pivot area up towards the frame with a dead blow hammer while pushing the pin in.

      This should align the hole and allow the pin to go right in.

      Insert the pin and fasten it with a new 3/8" E-clip.

   **Note:** This is the most difficult and dangerous part of the job.

   Use eye protection while doing this and ensure your hands won't be damaged if the spring flies back while getting it over the hook.

   Focus on applying steady force with as much leverage as possible to extend the spring back along the swingarm.

   - One trick is to use a strong line looped through the hook as a pulley.
   - Another trick is to bend the spring enough back and forth to insert pennies between the coils, which holds it in an extended position.

     Then loop the spring over the hook and pull the pennies out with pliers.
5. Check the operation of the kickstand a few times.

   Ensure that it operates smoothly.

   Ensure the kickstand sensor detects the position of the kickstand, by checking the interlock indication on the dash while the bike is keyed on.
6. Put the kickstand down before letting the motorcycle off the lift to rest on it.

**[Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Removal)**

**Tools**

- [Center lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) or stand.
- Large flat-blade screwdriver or specialized tool like [drum brake spring pliers](https://www.google.com/search?q=drum+brake+spring+pliers) for spring removal and replacement.
- E-clip tool (or needlenose pliers) for the 3/8" E-clip.

**Steps**

1. Place the motorcycle on a center lift or stand.

**Spring Before Pin**

1. Pull the spring off of the kickstand hook with a large flat blade screwdriver or a specialized kickstand spring release tool.

   Raise the kickstand to the stowed/horizontal position, to reduce spring tension.

   | | |
   | --- | --- |
   | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Be extremely careful working with the kickstand spring as it is under high tension. |

   A specialized tool makes this easier.
2. Remove the pivot pin.
3. Remove the kickstand.

**Pin Before Spring**

1. Remove the pivot pin.
   1. Pull the E-clip off of the inside of the pivot.
   2. Raise the kickstand to the stowed/horizontal position, to reduce spring tension.
   3. Go to the left side of bike.
   4. Wiggle the kickstand while tapping the pivot pin from underneath with *for example* a soft faced hammer.
   5. Continue to wiggle the kickstand while gripping the pin until it slides out.

      Often comes out by hand with a rag.
2. Carefully slide kickstand away from frame and unhook springs from frame.

   The kickstand will still be under some tension from both springs, inner and outer.

### [Footpegs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Footpegs)

Zero footpegs are cast aluminum pieces, mounted on identical hinges so are interchangeable across models.

**Mounting**

The mount bracket uses a custom clevis (10mm ⌀ with 40mm working length and 45mm overall length), secured with a retaining E-clip (3/8" or 9.5mm inner ⌀).

![Rider footpeg mount spring](../images/Rider-footpeg-spring.png) ![Rider footpeg clevis pin](../images/Rider-footpeg-clevis-pin.png)

**Repair**

The footpegs' aluminum casting is relatively brittle, and the pegs tend to break rather than bend.

See [Footpeg Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Footpeg_Replacement).

**Reference**

["The pegs are the exact same part used by the Buell XB models (except for the Ulysses), and as the passenger pegs on the 1125R models. They are "sacrificial lambs" to protect the rest of the frame."](http://electricmotorcycleforum.com/boards/index.php?topic=7851.30)

["Any pegs made for the 2008-2009 Suzuki RMZ450 should fit the DS,DSR,FX models"](https://www.electricmotorcycleforum.com/boards/index.php?topic=9937)

#### [Rider Footpegs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rider_Footpegs)

These [Footpegs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Footpegs) are only installed for the rider, versus [Passenger Footpegs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Passenger_Footpegs).

| | |
| --- | --- |
| **Sport Footpegs** <br> Installed on S/SR/FXS models. <br> Constructed as a cylindrical smooth-surfaced cast aluminum piece with a corrugated upper surface for some grip. <br> They are spring-loaded. <br> There is a hole at the end of the rider footpegs, with/for feeler stud measuring M6X16 with a DIN 1587 M6 18-8 cap/acorn nut. <br> ![Sport Footpegs underside](../images/Footpegs-sport-right-underside.png) *Sport Footpegs underside* <br> **Dual Sport Footpegs** <br> Installed on DS/DSR/FX models. <br> Constructed as a mildly-cleated rough-finish cast aluminum piece with a wide flat surface mounted horizontally. <br> They are spring-loaded. <br> Because of their construction, these actually offer less legroom than the sport footpegs. | ![S and DS footpegs compared](../images/Footpeg-comparison.gif) *S and DS footpegs compared* |

![Rider footpegs mounting bracket](../images/Footpegs-rider-mounting-bracket.png) *Rider footpegs mounting bracket*

##### [Rider Footpeg Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rider_Footpeg_Removal)

![footpeg retaining clip and tool](../images/Footpeg-retaining.jpeg) *footpeg retaining clip and tool*

**Tools**

- Snap Ring / E-Ring pliers (needlenose pliers are a common if less easy substitute).
- (Optional) 7mm Allen key to remove the clevis bracket from the frame.

**Steps**

1. Gently spread the gap in the retaining E-ring using the pliers until it slides over the end of the pin, and remove it.

   This clip is on the lower end of the footpeg retaining pin.
2. Pull the retaining pin up and out.

   Hold and pull the pin spring and footpeg as the pin comes out.
3. (Optional) Use the 7mm Allen key to remove the bolt through the clevis bracket that fastens it to the frame.

**References**

[How to Remove Zero Footpegs + Relocation Ideas](https://www.youtube.com/watch?v=9OdBkfS_qbs) by NewZeroLand on Youtube

#### [Passenger Footpegs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Passenger_Footpegs)

Passenger [footpegs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Footpegs) are ergonomically identical to the sport [rider footpegs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rider_Footpegs), since passenger geometry requires reduced legroom and a forward foot angle on the rest.

They are not spring-loaded.

They lack the hole for the feeler stud that the rider footpegs use.

![Sport Rider Footpegs vs Passenger Footpegs](../images/Footpegs-sport-passenger-peg-comparison.png) *Sport Rider Footpegs vs Passenger Footpegs*

![Passenger Footpegs Stowed](../images/Footpegs-passenger-stowed.png) *Passenger Footpegs Stowed*

**Mounting**

The passenger footpegs hinge on the [passenger footpeg bracket](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Passenger_Footpeg_Bracket) which mounts to the frame.

They use an additional installed pin and custom clip plate to secure the passenger pegs in either the stowed or out position (vertical and horizontal, respectively).

##### [Passenger Footpeg Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Passenger_Footpeg_Removal)

![footpeg retaining clip and tool](../images/Footpeg-retaining.jpeg) *footpeg retaining clip and tool*

**Tools**

- Snap Ring / E-Ring pliers (needlenose pliers are a common if less easy substitute).
- 13mm hex side or socket wrench (for the bracket).

**Steps**

1. Gently spread the gap in the retaining E-ring using the pliers until it slides over the end of the pin, and remove it.

   This clip is on the lower end of the footpeg retaining pin.
2. Pull the retaining pin up and out.

   Hold and pull the pin spring and footpeg as the pin comes out.
3. (Optional) Remove the bracket
   1. Loosen the upper bolts mounting the footpeg brackets to the frame.

      **S-platform:** Reaching these bolts from the rear is easiest since they are on the inside of the frame.
   2. Loosen the lower bolts mounting the footpeg brackets to the frame.

      **S-platform:** These face the motor and allow very low overhead.

      A side wrench is recommended, and a ratcheting version preferred.
   3. Remove the bolts and then the brackets.

**References**

[How to Remove Zero Footpegs + Relocation Ideas](https://www.youtube.com/watch?v=9OdBkfS_qbs) by NewZeroLand on Youtube

### Seat

#### [S Platform Seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Seat)

![Zero S Seat Pan](../images/2013-zero-s-seat-pan.png) *Zero S Seat Pan*

The S Platform seat is a proprietary design and fitment.

**Seat retaining features**

- A metal bracket with holes for retaining bolts that mount through the frame from the outside.

  The bracket also serves to align the seat horizontally since the outer sides of the bracket must slide directly along the inside track of the frame.

  ![Zero S Seat Bracket](../images/2013-zero-s-seat-bracket.png)![Zero S Seat Bracket](../images/2013-zero-s-seat-bracket-side.png)

  The bracket's part number is 20-0508307 and when separately ordered has been observed to have slotted holes to join to the seat for some adjustability.
- In front and center, a pair of catches engages the frame's [Y-shaped centerpiece](#Y-Shaped_Underseat_Frame) under a pair of pins.
- In front on the lowest outside edge, a pair of tabs point downwards that should slide inside the frame rails.

  Without some care, these easily wind up outside the frame, flexing the seat pan and scuffing the frame lightly with plastic debris.

**Under The Seat**

![2016 DSR tail layout](../images/Dsr-under-seat.JPG) *2016 DSR tail layout*

- The large [controller](#Controller) dominates the space underneath the seat, on the lowest part of the tail structure.

  There's no room around the controller for anything but its cabling and a conduit for tail lighting.
- In front, the 12V fuse block is the main item to access.

  There are cables between the battery and the controller; the MBB and DC-DC converter are beneath these cables.
- Behind the [controller](#Controller) is the [tail wiring](#Tail_Wiring) area which has a little room for a tire patch kit or some tools.

  Of course, storing tools for removing the seat there is counter-productive.

**Dimensions**

- Seat
- Seat Bolts

  M8 with 1.25mm thread, 50mm long with a round end for aligning the seat bracket with the frame.

  With the top rack installed, the diameter of the hole around the head is slightly under 15mm, with a maximum offset of about 12mm.
- Seat Bracket Bolts to Seat Pan

#### [X Platform Seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Seat)

The FX/FXS seat is closer to an offroad "plank" seat, allowing the rider to pick their position forward or back.

![2013 and 2018 FX seats](../images/2013-and-2018-fx-seats.jpg) *2013 and 2018 FX seats*

![2013 FX seat](../images/2013-fx-seat.jpg) *2013 FX seat*

![2018 FX seat](../images/2018-fx-seat.jpg) *2018 FX seat*

**Variants**

- 2010-2013 X seat

  This seat offers additional height and free movement front to back.

  "The 2013 seat is also known as the off-road seat. p/n 24-01596 - SEAT ROODIN RD-M1231-K BLACK. Taller riders tend to like it as well if their butts hit the bump of the contoured seat." per [comment on Facebook](https://www.facebook.com/groups/zmcowners/permalink/1767787513290449/?comment_id=1768533619882505&comment_tracking=%7B%22tn%22%3A%22R0%22%7D)
- 2014-current X seat

  Has a cutout / dip.

  Tapers more at the back (pointy), and flows down the sides a bit more too. Basically it's more contoured to the bike.
- Corbin made a low seat for 2010-2012 X platform models.

**Mounting**

M8×25 bolts are listed as the bolts that run through the tail subframe to the bracket at the rear of the seat to hold it in place.

**Replacement Fitments**

Harlan at [Hollywood Electrics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Hollywood_Electrics) reports that [the FX seat is an exact match](https://www.facebook.com/groups/zmcowners/permalink/1384661314936406/?comment_id=1385815301487674&reply_comment_id=1385986874803850&comment_tracking=%7B%22tn%22%3A%22R4%22%7D) for the 2005-2007 Honda [CRF-450](https://en.wikipedia.org/wiki/Honda_CRF_series).

#### [Seat Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Seat_Removal)

This removes the [seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Seat) from [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) bikes.

**Video Guide**

[Zero motorcycle - How to remove your seat](https://www.youtube.com/watch?v=T80siAHG7Z8) by [Alternative Standard on YouTube](https://www.youtube.com/channel/UCw9faNzFHkqXDsybkH7Qqig)

**Notes**

- Unload any luggage racks before taking the seat off for an extended period of time to avoid stressing the racks.

  When luggage racks are installed, the seat bolts are load bearing (or at least damping).
- An M8-1.25×55mm socket cap bolt with a 6mm Allen head can be used if the kit bolt is lost.

**Tools**

- **2015+:** T45 Torx wrench (for seat bolts).
- **2013-2014 (with top or side racks):** 5mm Allen key (for seat bolts).

**Steps**

1. *When luggage racks are installed* Remove the top case and/or side cases to ensure the rack is unloaded.
2. Remove the M8-1.25×55 seat bolts.

   Push the seat down and forward as needed to help ease out the bolts.

   ![Seat Fasteners](../images/TOPRACKKIT10-0692107_seatfastener.jpg) *Seat Fasteners*

   ![Seat Fasteners with Top Rack Installed](../images/MY2016DSR_seatfastener_withtoprack.jpg) *Seat Fasteners with Top Rack Installed*
3. Pull the seat back a couple of inches and then upwards.

#### [Seat Install](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Seat_Install)

This installs the [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) models' [seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Seat).

**Tools**

- **2015+:** T45 Torx wrench (for seat bolts).
- **2013-2014 (with top or side racks):** 5mm Allen key (for seat bolts).

**Steps**

1. *When luggage racks are installed* Remove the top case and/or side cases to ensure the rack is unloaded.
2. Place the seat on the tail slightly to the rear of where it will sit.

   Ensure that the pan's horn-shaped catches will slip under the frame's Y-shaped centerpiece pins.
3. Push the seat forward and down to sit in place.
4. Visually align the holes of the seat bracket with the seat bolt holes.

   Align the seat's bracket with the frame holes to avoid wear.

   Align the seat's tabs between the frame rails to avoid stressing the seat pan and marring the frame.

   If the top rack is installed, too, check the alignment of that as well to avoid wear trying to thread the bolts.
5. Insert the seat bolts, gently engaging while checking for cross-threading.

   Check for alignment again while the bolt head encounters the seat bracket.

   Press down and forward on the seat as needed to help align and tighten the bolts.

   ![Seat Fasteners](../images/TOPRACKKIT10-0692107_seatfastener.jpg) *Seat Fasteners*

   ![Seat Fasteners with Top Rack Installed](../images/MY2016DSR_seatfastener_withtoprack.jpg) *Seat Fasteners with Top Rack Installed*
6. Tighten the bolt head against the frame surface to hold it in place but do not over-tighten.
7. *When luggage racks are installed* Re-install the top case and/or side cases.

### [Panel Material](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Bodywork_Material)

[Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) body panels are made from [ABS plastic](https://en.wikipedia.org/wiki/Acrylonitrile_butadiene_styrene).

**2013-2016**

The plastics' color is molded-in, and so it fades over time with sun exposure. On the other hand, they're relatively inexpensive to replace from Zero; ask your dealer.

Some use [Plexus plastic cleaner](http://www.plexusplasticcleaner.com/about.html) to keep them polished successfully.

[POLYTROL Colour restorer](http://owatrol.com/en/all-our-products/7932-polytrol.html) could help with [color restoration](http://electricmotorcycleforum.com/boards/index.php?topic=6933.msg56801#msg56801).

[Retr0bright](https://en.wikipedia.org/wiki/Retr0bright) solution developed for restoring 1980's yellowed ABS personal computer chassis material *may* be of use, unconfirmed.

**2017+**

The plastics as of this model year are painted rather than molded-in.

### [Tank Plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Plastics)

![2014 SP Tank Plastics (left)](../images/Tank-plastics-sp-left.png) *2014 SP Tank Plastics (left)*

![2014 SP Tank Plastics (right)](../images/Tank-plastics-sp-right.png) *2014 SP Tank Plastics (right)*

The 2013+ [SDS Platform Frame](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Frame) features a "tank" area cradled by the two front frame spars and covered by plastic bodywork.

As delivered, it offers a storage compartment, but can also accommodate systems accessories like the OEM Power Tank battery upgrade or chargers.

All of the bodywork for this area serve the same ergonomic functions of a traditional motorcycle's fuel tank, allowing grip for maneuvering.

**Fasteners**

Zero plastics all are fastened with blackened M5x15mm mushroom cap socket head bolts using a 3mm allen key wrench.

All have black plastic washers with 5mm inner diameter, 10mm outer diameter, roughly 1mm thick.

**Removal**

See [Tank Plastics Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Plastics/Removal)

**Construction**

All variants of the tank plastics for have identical side pieces and a black centerpiece in soft plastic with a relatively rough finish.

The stock centerpiece for 2013-2016 models is a bin container with two drain holes for collected moisture, with a soft bin held together with a simple zipper that anchors via hook-and-loop patches at the bottom of the bin as well as a loop cord that hooks through the front helmet lock.

The bin delivered per model year is different and varies in quality. 2013 seemed to have better construction than 2014-2015 years, and 2016 is somewhere between.

As of 2017, the stock centerpiece is a locking storage container with a spring-loaded hinge at the front so it swings forward to open.

The Power Tank and Charge Tank have tank plastic options which can be bought separately or selected for color customization. Both use a relatively flat surface for the centerpiece, and the Charge Tank has a cutout for a [J1772](https://web.archive.org/web/2025/https://zeromanual.com/wiki/J1772) inlet hold with built in waterproof cover with a spring-loaded hinge.

![2014 SP plastics - dewelding](../images/Zero_Tank_Plastics_Dewelding.png) *2014 SP plastics - dewelding*

**Separating**

The join between the centerpiece and side pieces of a Zero tank plastic assembly is made by plastic weld using a soldering iron into soft hollow plastic pins on the centerpiece that melt and flatten around a lock washer onto holes in the side pieces.

You can break these welds using a relatively careful use of a pair of pliers to basically grip hard and twist on them until they break.

It's a slightly frustrating process but pretty quick to achieve, in about an hour. A soldering iron or extremely narrowly-focused heat gun can help the process but try not to risk damaging the plastics from overheating.

The original join process can be repeated for the new centerpiece.

Also, this means that the plastic centerpiece you remove will not be re-joinable.

**Repair**

See [Tank Plastics Repair](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Plastics/Repair) for a way to re-join tank plastics that have been de-welded.

### [Tail Plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tail_Plastics)

The tail plastics on the SDS platform enclose the tail subframe and support the rear brake/running lights and the license plate holder with its turn signals.

#### [Tail Plastics Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tail_Plastics_Removal)

This removes the [S-Platform Tail Plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tail_Plastics) from the bike.

**Note:** The author documented the reassembly; removal was inferred. Confirmation would be helpful.

![Zero S tail subframe with upper plastics removed](../images/2015-zero-s-tail-subframe-uncovered.png) *Zero S tail subframe with upper plastics removed*

**Video Guide**

[Zero motorcycle - How to remove your tail plastic](https://www.youtube.com/watch?v=GJeyMEy60s0) by [Alternative Standard on YouTube](https://www.youtube.com/channel/UCw9faNzFHkqXDsybkH7Qqig)

**Notes**

You'll be disconnecting the rear lighting wiring and removing the tail subassembly, and then removing the tail plastics from that.

The lower plastics removal are particularly difficult, even for dealers!

**Tools**

- 3mm, 4mm, 6mm Allen wrenches.
- For the seat bolts: T45 Torx wrench (without top rack) or 5mm Allen wrench (with top rack).
- Phillips screwdrivers.
- Needle nose pliers.

**Steps**

1. [Remove the seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Seat_Removal).
2. Remove the black seat pan bolts and nylon washers with the 3mm Allen wrench

   These are located lower on the side, near the hollow frame tube.

   There are 5 pairs of bolts to remove (documented via reassembly analysis):

   ![ZeroTail01.jpg](../images/ZeroTail01.jpg) ![ZeroTail02b.jpg](../images/ZeroTail02b.jpg)
3. Use a Philips screwdriver to unscrew the bolt holding down the rear of the plastic controller cover.
4. Cut the cable ties around the signal wires on the left side of the seat area behind the controller.
5. Disconnect the turn signal wires and brake light / plate light wires.

   Take a photo to record their connections for correct re-assembly.

   ![ZeroTail16.jpg](../images/ZeroTail16.jpg) ![ZeroTail17b.jpg](../images/ZeroTail17b.jpg)
6. Remove the 4 bolts that hold tail frame with a 6mm Allen wrench.

   This detaches the tail frame.
7. Remove the tail extension using a 4mm Allen wrench. Mind the turn signal wires that go through holes here; draw them through.

   ![ZeroTail15.jpg](../images/ZeroTail15.jpg)
8. Remove the black tail enclosure plastics from the cosmetic plastics via the tabs.

   There's also two clips at the end on top of the taillight.

   ![ZeroTail14.jpg](../images/ZeroTail14.jpg)
9. Use a Philips screwdriver to remove 5 screws holding the cosmetic plastics to the frame from underneath.

   ![ZeroTail04.jpg](../images/ZeroTail04.jpg)
10. Use a 3mm Allen wrench to remove the two screws holding the cosmetic plastics to the top of the frame.

    ![ZeroTail03.jpg](../images/ZeroTail03.jpg)

**Reassembly**

1. With the tail light off, bolt the top plastic to the metal frame.

   ![ZeroTail03.jpg](../images/ZeroTail03.jpg)
2. Clamp the bottom tail plastic and screw in the 5 screws that hold both pieces together

   ![ZeroTail04.jpg](../images/ZeroTail04.jpg)
3. Here is how the black tail plastic fit with the tail light.

   Notice the "zipper" down the middle.

   There's also a very small one on top of the tail light.

   On the outside are the tabs that clip into the cosmetic plastics.

   ![ZeroTail05.jpg](../images/ZeroTail05.jpg) ![ZeroTail06.jpg](../images/ZeroTail06.jpg)
4. Loosely bolt the end of the black tail plastic to the frame.

   Note the small nut that's between two fins of the controller.

   It can easily be held with a pair of pliers.

   ![ZeroTail07.jpg](../images/ZeroTail07.jpg)
5. Rotate the pieces up and temporarily (and loosely) attach them to the frame.

   ![ZeroTail08.jpg](../images/ZeroTail08.jpg) ![ZeroTail09.jpg](../images/ZeroTail09.jpg)
6. Bolt the tail light:
   1. Remove the temporary bolts from the previous step.
   2. Push a driver down through the plastic (because of the angle of the taillight bolts).

   ![ZeroTail10.jpg](../images/ZeroTail10.jpg) ![ZeroTail11.jpg](../images/ZeroTail11.jpg)
7. "Zip" the plastic back together.

   There's also a tab on top of the tail light that must be fitted properly.

   ![ZeroTail12b.jpg](../images/ZeroTail12b.jpg)

   I added duck tape to seal the interior of the compartment to keep it cleaner.

   ![ZeroTail13b.jpg](../images/ZeroTail13b.jpg)
8. Snap the clips on the cosmetic plastic.

   **NOTE:** It's not the cosmetic piece that should move but the black piece

   I found it helped to have one hand inside and one hand outside to fit the pieces together.

   There's also two clips at the end on top of the taillight.

   ![ZeroTail14.jpg](../images/ZeroTail14.jpg)
9. Loosely bolt the tail and fit the wires back through the small hole.

   ![ZeroTail15.jpg](../images/ZeroTail15.jpg)
10. Add a new zap strap and tidy things up.

    ![ZeroTail16.jpg](../images/ZeroTail16.jpg) ![ZeroTail17b.jpg](../images/ZeroTail17b.jpg)

    Note that before disconnecting the wires, I took a picture of the set up to be able to match the colours.

    In my case, red goes with green and white goes with grey (confirm locally). In the case of a 2018 SR, it was red/black to red and green/white to white.
11. Fasten all the loose bolts.

    ![ZeroTail18.jpg](../images/ZeroTail18.jpg)
12. (If applicable) Re-attach the top and side racks.

    ![ZeroTail19.jpg](../images/ZeroTail19.jpg)

### [Lower Plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Lower_Plastics)

Lower plastics for the SDS Platform involve two side pieces to direct air towards the motor, and one in front to cover the battery.

There is some provision for guarding the battery compartment against an impact from the front wheel in the case of a collision.

![2017 Zero S Lower Front Plastics](../images/2017-zero-s-battery-front.jpg) *2017 Zero S Lower Front Plastics*

**2012-2013**

Relatively angular and have their own bolt mount pattern.

**2014+**

Lower plastics have a sculpted re-design to deliver more airflow to the motor for cooling.

**2017+**

Single longbrick models (ZF6.5 and ZF7.2) have lower plastics with a latch and swinging hinge to access the storage area behind the half-size battery compartment.

#### [Lower Plastics Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Lower_Plastics_Removal)

This removes the lower side panel plastics from 2012+ S platform models.

**Tools**

- 3mm Allen key
- (2012-2013) Ball-point pen or similar for plastic push rivets.
- (2019+) PH2 phillips head screwdriver for the front panel.

**Steps**

1. Use the 3mm Allen key to remove the three M5 bolts holding each side panel: one at the top front corner, and one at each corner near the lower edge.

   ![Top Front Corner bolt (2014+)](../images/Lower_plastics_bolt1.jpg) *Top Front Corner bolt (2014+)*

   ![Lower Rear bolt (2014+)](../images/Lower_plastics_bolt2.jpg) *Lower Rear bolt (2014+)*

   ![Lower Front bolt (2014+)](../images/Lower_plastics_bolt3.jpg) *Lower Front bolt (2014+)*
2. Remove each side panel.

   ![Removing the bolts](../images/MY2016DSR_sideplastics_removal.jpg) *Removing the bolts*

   ![Side panel removed](../images/Lower_side_plastics_removed.jpg) *Side panel removed*
3. (Optional) Remove the 2 bolts on each side holding the front panel on and remove it.

   **2012-2013:** Use the ball-point pen or similar non-scratching pointed tool to push the center pin to release the plastic rivets on the front panel and remove it.

   **2013-2018:** Use the 3mm Allen key

   **2019+:** Use the PH2 Phillips head screwdriver to gently remove the plastic screws from the pop rivet, then pull the pop rivet out from the side slot.

**References**

Adapted from [this forum post](http://electricmotorcycleforum.com/boards/index.php?topic=4424.msg28648#msg28648).

## Steering

### [Ignition Lock](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Lock)

The ignition lock operates the [Ignition Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Switch).

**Location**

The ignition lock is mounted on the tripe clamp top in the center between the steering head and the dash.

The [Ignition Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Switch) connects to a [ZADI](http://www.zadi.com) motorcycle lock with a steering lock feature and parking light enable (although the parking light enable is not connected on the Zero).

**Key Blanks**

Key blanks can typically be ordered from a dealer.

Key blanks appear to be available generically as [JMA ZA9P1 FOR ZADI ZD23RCP](http://www.mrlock.com/jma-zadi-motorcycle-key-blanks/jma-key-blank-zadi-zd23rcp-za-9-p1).

In USA, calling them "Triumph" keys may help a locksmith find the right blank.

**Maintenance**

Occasional lock lubrication is recommended, and inspection of the wires for startup enable on the underside of the lock for reliability.

**Troubleshooting**

See [the faulty ignition switch troubleshooting guide](https://web.archive.org/web/2025/https://zeromanual.com/wiki/12V_Power_Always_On) for issues with this.

### [Tank Lock](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Lock)

The lock for the tank bag (2013-2016) or tank compartment (2017+) and possibly a helmet is keyed the same as the [Ignition Lock](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Lock).

**Mounting**

The tank bag lock (2013-2016) is mounted to the frame by two (M5?) bolts under the steering head.

It's very difficult to access without taking much of the frontend apart (as it should be, for theft deterrence).

**References**

[ZADI lock re-pin](https://electricmotorcycleforum.com/boards/index.php?topic=9330)

### [Mirrors](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Mirrors)

| | |
| --- | --- |
| ![2012-2014 Mirrors (side) on a DS](../images/Mirror-side-2012-ds.png) *2012-2014 Mirrors (side) on a DS* | ![2015+ mirrors (side) on a DSR](../images/Mirror-side-2016-dsr.png) *2015+ mirrors (side) on a DSR* |

**Design**

Pre-2015 ([Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1)) Zeros use an angular mirror with a ball mount joint that allows rotating the mirrors 360 degrees.

Many riders turn the mirrors upside down for a little wider visibility around the shoulder/arms.

2015+ ([Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) and [Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3)) Zeros use a mirror stalk with an inboard ball mount with about 30 degrees of freedom from the stalk.

**Mount**

Zero mirrors are mounted from the handlebars with Yamaha/Ducati-style bolt fitting.

The bolt/thread specification is M10x1.25, left-hand-threaded on the right side and standard right-hand-threaded on the left side.

**Maintenance**

(pre-2015) Check that the set screw holding mirror position holds it firmly.

Use a corrosion inhibitor or thread-locker for the set screws and the mount threading since these are weather-exposed.

See [Third-Party Mirrors](Common_Modifications.md#Third-Party_Mirrors "Common Modifications") for workable/tested replacements.

### [Handlebar](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Handlebar)

Zero's models all steer with a [handlebar](https://en.wikipedia.org/wiki/Motorcycle_handlebar).

S/SR and FXS models share a shorter, sportier handlebar shape.

DS/DSR and FX models share a wider, straighter handlebar shape.

Both S/FXS and DS/FX style handlebars are standard through-bars.

**Diameters**

- 1 1/8" (28mm) ⌀ center bar.
- 7/8" (22mm) ⌀ outer bar.

| Models | Years | Width | Rise | Pullback |
| --- | --- | --- | --- | --- |
| S,SR,FXS | 2013-present |  |  |  |
| DS,DSR,FX | 2013-present |  |  |  |
| SRF,SRS | 2020-present |  |  |  |

**Control-Indexing Holes**

- (1) 3/16" ⌀ on the left for the switchgear, 6.5" from the end of the bar.
- (1) 3/16" ⌀ on the *right inner* for the [throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle), 7 3/16" from the bar end.
- (1) 5/32" ⌀ on the *right outer* for the switches, 6" from the bar end.

**References**

- [Changing to non OEM handlebars (‘15 FX)](https://www.electricmotorcycleforum.com/boards/index.php?topic=10043)

#### Handlebar Clamps

The SDS and XMX platform handlebar clamps are 2" by 1 1/8" (28mm) for the entire line of models, clamped with M10 cap screw bolts (35mm length; possibly 50mm?).

#### Handlebar Switch Assemblies

The switch assemblies are fastened with TT20 (1/4") tamper-resistant Torx bolts through the underside.

#### Handgrips

Handgrips have a Zero logo on them but otherwise are reasonably good stock grips for the 7/8" (22mm) handlebar width at the end of the bars.

#### Bar Ends

For 2014+ models, any bar end accessories that match the 14mm inner diameter will fit.

![2014+ stock bar end plugs](../images/2016_end_plugs.png) *2014+ stock bar end plugs*

The stock bar ends are round plastic bumpers held in by plastic threads, so can be removed with a little twisting and pulling.

**2013 models**

Bar ends are covered by the grip so are not easily changed without changing the grips.

Zero did offer heated grips for these models but dropped them after changing the bars in 2014.

### [Brake Lever](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Brake_Lever)

Zero motorcycles have a right-hand lever for the front brake, as is common for motorcycle designs.

![Brake Lever](../images/Brake_Lever.png) *Brake Lever*

![Brake Lever Switch](../images/Brake_Lever_Switch.png) *Brake Lever Switch*

**Primary adjustment**

The brake lever has a dial for adjusting the lever position relative to pad pressure and rider finger reach.

Set it however lets you operate it comfortably and safely.

**Brake Light and Regen Switch**

A set screw on the inside of the lever adjusts how a micro-switch is depressed.

The micro-switch is what activates the rear brake light and the "braking regen" mode at the same time.

Any adjustment or replacement of the brake lever should be followed by recalibrating this set screw to get the desired effect.

Too much free play and the switch will activate when going over bumps and result in a slightly jerky ride.

There is some guidance on how to adjust this: [Brake Lever Adjustment to Regen Before Pad Contact](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Lever_Adjustment_to_Regen_Before_Pad_Contact).

**NOTE:** It seems like there's small difference in how this set screw is secured in stock lever compared to replacement lever (2016 SR), even though they look identical.

I wasn't able to adjust this screw on stock lever, however replacement lever adjusts with no issues.

You will need 7/64 SAE hex key to adjust.

Use some light threadlock compound (Blue Loctite will do) to fix the set screw in the desired position if it seems to move too freely out of the desired range.

**References**

- [Front brake tightness?](https://www.electricmotorcycleforum.com/boards/index.php?topic=9755)

**Adjustment**

See [Front Brake Lever Adjustment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Brake_Lever_Adjustment)

**Removal, Repair**

See [Front Brake Lever Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Brake_Lever_Replacement)

### [Triple Clamp](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Triple_Clamp)

The [triple clamp tree](https://en.wikipedia.org/wiki/Telescopic_fork#Triple_Tree) attaches the fork tubes to the [frame](#Frame) via the [steering head bearing](#Steering_Head_Bearing).

The design and fitment changed from MY 2013-2014 to MY 2015+, when the forks changed from FastAce to Showa.

**Upper Assembly**

This sits atop the [steering head](#Steering_Head), joining the forks at the top, and supports the [handlebars](#Handlebars), [ignition switch](#Ignition), [dash](#Dash), and [headlamp](#Headlamp).

**Lower Assembly**

This inserts upward through the [steering head](#Steering_Head) tube, joining the forks below the tube, and supports the [headlamp](#Headlamp) bracket and the high fender for DS/DSR/FX models.

The upper assembly and lower assembly join around/through the [steering head](#Steering_Head).

### [Steering Head](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Steering_Head)

The steering head is the tube in the head position of the frame that mounts the fork steerer tube.

For 2014+ S and X-platform Zeros, the inner diameter of the steering head is 55mm for a steering tube size of 1in (25.4mm).

**Steering head fastener stack (top to bottom)**

1. Steering Stem Thin Nut (M27⨉1.5mm, 8mm depth); apply a 41mm hex socket.
2. Washer 41 - 27.5mm⌀, 2mm thickness (reportedly not present on 2018+ models)
3. Steering Stem Lock Nut (M30⨉1.5mm)
4. Bearing Lip Seal (55mm OD)
5. [Steering Head Bearing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Steering_Head_Bearing) (facing up)
6. Lower Triple Clamp Assembly Tube
7. [Steering Head Bearing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Steering_Head_Bearing) (facing down)
8. Bearing Lip Seal (55mm OD)

#### [Steering Head Bearing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Steering_Head_Bearing)

The steering head bearing is a [tapered roller bearing](https://en.wikipedia.org/wiki/Rolling-element_bearing#Tapered_roller) in the frame's [steering head tube](https://en.wikipedia.org/wiki/Head_tube).

**Troubleshooting**

- Steering stickiness or wobble may indicate an inadequately greased steering head bearing or a worn bearing.

| Platform | Years | Dimensions | Stock Model | Part # | Description |
| --- | --- | --- | --- | --- | --- |
| S,X | 2014-2018 | ID: 30mm <br> OD: 55mm <br> Width: 17mm | Koyo SAC3055-1 | ZM20-06068 | Angular-contact caged ball bearings |

**Replacement**

See [Steering stem bearing replacement ('14-'17, all models)](http://electricmotorcycleforum.com/boards/index.php?topic=7717) described for a 2014FX.

**Reference**

[ZeroDS head bearing (2015)](http://electricmotorcycleforum.com/boards/index.php?topic=6762)

[DSR 17 steering head bearings](http://electricmotorcycleforum.com/boards/index.php?topic=7417)

[Steering stem bearing replacement ('14-'17, all models)](http://electricmotorcycleforum.com/boards/index.php?topic=7717)

### [Front Fender](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Front_Fender)

The front fender covers the front wheel and acts as a mudguard against the front electrics and the front panel of the battery casing.

- The S/SR front fender is a [sporty low fender](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Low_Front_Fender) colored or painted panel like the [tank plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Plastics) that hugs the tire.
- The DS/DSR/FX/FXS front fender is an ABS plastic [dual sport high fender](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/High_Front_Fender).

#### [Low Front Fender](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Low_Front_Fender)

The S and SR models have a low front fender.

The low front fender is a colored or painted panel like the [tank plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Plastics) that hugs the (17") front tire.

**Mounting**

The low front fender bolts onto the lower front fork cast aluminum bracketing.

The mounting uses 4 (2 per side) M5x15 bolts with a black finish, with a 3mm Allen/hex key (H3) drive with black plastic washers.

The holes are 85mm apart (centerline-to-centerline), and the width across the brackets measured from the outside face is 192mm across the wheel (taken from a 2020 DSR).

**Transfer to other models**

It bolts directly onto the FXS' lower forks around its tire even though the FXS comes with a dual sport fender.

See [Low Front Fender Swap](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Low_Front_Fender_Swap) for how to adapt this to the DS and DSR models.

#### [High Front Fender](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/High_Front_Fender)

The DS, DSR, and FXS models have a dual sport / high front fender.

The dual sport fender attaches to the underside of the front fork triple tree.

**Mounting**

4 holes in a rectangular shape 58mm (2.3in) wide and 50mm (1.95in) front to back (center to center).

The bolts are (at least through 2016) M5x15mm button head socket screw for a 3mm Allen key.

The bolts on 2017?-present models are M5x15mm flanged socket head screws for a T25 Torx key.

**Transfer**

This fender also fits a S/SR model.

A Honda or Yamaha dual sport fender should fit this pattern without modification.

## Wheels

### Wheel Maintenance

#### [Tire Pressure Check](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Tire_Pressure_Check)

Maintain minimum pressure per the [official manual](Official_Owners_Manual.md "Official Owners Manual").

**General guidelines**

- *Higher* tire pressures help *stability* and *reduce rolling resistance* with a passenger or a lot of luggage, but *lower* pressures help on rougher/gravel surfaces.

  Excessive tire pressure can make the tire too sensitive to sharp debris or potholes, and increases the risk of a puncture.

  45psi is where this definitely becomes a concern; modulate depending on your riding, and definitely use much lower pressures for offroading.
- Official recommendations are for *cold* tires, which means when they haven't been ridden in a few hours.

  As tires warm up from riding, pressure increases due to the interior air heating from friction and mechanical work on the tire by the road against the wheel.

### [Front Wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Front_Wheel)

The front wheel for [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) models has a few variations and sizes (mirroring the [rear wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel)).

- 2013-2014 DS and FX models have spoked construction, a holdover from [Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1) offroad models.
- 2013-2014 S and SR models have a very simple construction that is like cast/mag wheels but seems welded, a holdover from the 2012 S model.
- 2015+ FX models retain the spoked construction but are revised.
- 2015+ DS and DSR models have cast/mag wheel construction and 19" diameter.
- 2015+ S, SR, and FXS models have cast/mag wheel construction and 17" diameter.

| Years | Models | Construction | Diameter | Dimensions |
| --- | --- | --- | --- | --- |
| 2013+ | FX | Spoked | 21" |  |
| 2013-2014 | DS | Spoked | 19" |  |
| 〃 | S, SR | Cast/mag with welds | 17" |  |
| 2015+ | DS, DSR | Cast/mag | 19" |  |
| 〃 | S, SR, FXS | 〃 | 17" |  |

#### [Front Wheel Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Wheel_Removal)

**Video Instruction**

[Zero DS front wheel removal](https://www.youtube.com/watch?v=ihYVS3E0NVs) by Nigel Morris on YouTube:

[Zero Motorcycles: Front Wheel Removal 2016 DSR](https://www.youtube.com/watch?v=6wrPLi9Yags) by [E Shattow on YouTube](https://www.youtube.com/channel/UC3JGiY70BCPHoecAGEYEvTA):

**Tools**

6mm Allen Wrench - Axle bolt (M17)

5mm Allen Wrench - Pinch

13mm Socket - Brake calipers

**Steps**

1. Loosen both brake caliper bolts using the 13mm socket.
2. Loosen both *right* pinch bolts using the 5mm allen wrench.

   Alternate slightly, turning each counter-clockwise.
3. Loosen the axle bolt using the 6mm allen wrench.
4. Loosen both *left* pinch bolts using the 5mm allen wrench.

   Alternate slightly, turning each counter-clockwise.
5. *Securely* lift the front wheel.
6. Remove both brake bolts using the 13mm socket, and lift and secure the [brake caliper](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_caliper) without stressing the brake lines.
7. Continue to back off the pinch bolts, but do not remove, using the 5mm allen wrench.
8. Remove the axle bolt and outer spacer using the 6mm allen wrench.
9. Replace the axle bolt with the 6mm allen bolt, turning several turns inward, without the outer spacer.
10. Push on the axle bolt while encouraging the *left* side of the axle out.

    Support the wheel to reduce binding!
11. Remove the axle.
12. Remove the wheel.

#### Front Axle

**TODO measurements**

#### Front Tire

See [Stock Tires](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Stock_Tires).

#### [Front Bearings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Front_Bearings)

The [front wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Front_Wheel) has 2 bearings of the same size as the 3 [rear bearings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Bearings) (see table there for sizing).

**TODO**

Spacer specs

#### [Front Bearing Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Bearing_Replacement)

This replaces the [front wheel bearings on Gen2 models](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Front_Bearings).

**Tools**

- 6mm Allen Wrench - Axle (M17)
- 5mm Allen Wrench - Pinch
- 13mm Socket - Brakes
- Bearing Press Tool/Kit

**Steps**

1. [Remove the Front Wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Wheel_Removal)
2. Remove the spacers, then the dust seals, from each side and clean.
3. Press the bearings out from the opposite side.

   A socket extension works well, alternating around the perimeter.
4. Clean the inner wheel.
5. Press the new bearings in, aligning with the inner axle tube.

   A large socket works well to press only on the *outer* bearing.
6. Replace the dust seals.
7. Return the wheel to the bike.
8. Aligning the axle with the spacers, press the axle back into the forks.
9. Expand the brake calipers to prepare for remounting.
10. Remount brake caliper with the 13mm socket to the correct torque.
11. Return the outer spacer and make the axle bolt snug with the 6mm allen wrench.
12. Alternate tightening each 5mm pinch bolt.
13. Ensure proper wheel movement.
14. Tighten *left* pinch bolts to the correct torque using the 5mm allen wrench.
15. Tighten the 6mm Axle bolt to the correct torque.
16. Tighten *right* pinch bolt to correct torque using the 5mm allen wrench.
17. Ensure smooth movement.
18. Pump the brakes to return to proper action.
19. Lower the front wheel.
20. Confirm torques.
21. *Test ride!*
22. Reconfirm torques.
23. Paint the bolt heads to so that any loosening is detectable.

### [Rear Wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel)

The rear wheel for [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) models has a few variations and sizes (mirroring the [front wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Front_Wheel)):

- 2013-2014 DS and FX models have spoked construction, a holdover from [Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1) offroad models.
- 2013-2014 S and SR models have a very simple construction that is like cast/mag wheels but seems welded, a holdover from the 2012 S model.
- 2015+ FX models retain the spoked construction but are revised.
- 2015+ S, SR, FXS, DS, and DSR models have cast/mag wheel construction and 17" diameter.

| Years | Models | Construction | Diameter | Dimensions |
| --- | --- | --- | --- | --- |
| 2013+ | FX | Spoked | 18" |  |
| 2013-2014 | DS | Spoked | 17" |  |
| 〃 | S, SR | Cast/mag with welds | 〃 |  |
| 2015+ | DS, DSR | Cast/mag | 〃 |  |
| 〃 | S, SR, FXS | 〃 | 〃 |  |

#### Rear Tire

See [Stock Tires](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Stock_Tires).

#### [Rear Wheel Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Wheel_Removal)

Pulling out the axle and removing the rear wheel is straightforward; the complexity is in re-assembly: see [Rear Wheel Install](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel_Install).

**Items to note for re-assembly**

Note how the caliper sits against the swingarm.

Note the order and arrangement of the spacers.

**Video Guide**

[Zero Motorcycles: Rear Wheel Removal 2016 DSR](https://www.youtube.com/watch?v=CiZem4Q9uh4) by [E Shattow](https://www.youtube.com/channel/UC3JGiY70BCPHoecAGEYEvTA)

**Tools**

- 27mm socket
- Breaker bar

**Instructions**

1. Place the motorcycle on a [lift or rear stand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) so the wheel spins freely.
2. Mark/photograph where the alignment marks reside on each side of the axle for re-alignment when re-installing the wheel.

   ![Rear Axle Nut](../images/Rear_Axle_Nut_and_right_adjustment_bolt.jpeg) ![Rear Axle Spacer](../images/Rear_Axle_Spacer_and_left_adjustment_bolt.jpeg)
3. Loosen the rear axle nut on the right side (27mm) with the breaker bar.
4. Remove the rear axle nut.
5. Pull the axle part-way out so that the wheel can be moved forward enough to loosen the belt.
6. Pull the belt off of the rear sprocket and let it hang outside of the swingarm slightly to avoid interfering with the wheel.
7. Pull the axle through the wheel from the left side.

   Pay attention to the brake caliper: it's attached via the axle, and when the axle is removed the caliper, etc, will come loose.
8. Set aside the spacers with alignment marks, noting which goes on which side.
9. Set aside the axle and axle nut.
10. Pull the wheel out behind the swingarm.

    The license plate tail holder will likely require rolling the wheel out at an angle to clear it.

#### [Rear Wheel Install](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Wheel_Install)

Re-installing the rear wheel requires somewhat careful fitment of the wheel, spacers, ABS sensor (2015+), and brake calipers within the swingarm.

Pay attention while removing the wheel to have this arrangement in mind to avoid confusion.

Any play in the caliper position or the wheel itself could have a dramatic and damaging effect on the motorcycle while riding.

**Tools**

- 27mm socket
- Torque wrench set to 75ft-lbs (102Nm)
- (Optional) rubber mallet to nudge the axle

**Instructions**

- Also see [Belt Adjustment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belt_Adjustment)

1. Ensure that the axle has grease applied if it is dry, to minimize friction and wear against it under load.
2. Push the axle through the alignment bracket and left swingarm until flush on the inside of the left swingarm.
3. Place the rear brake caliper holder onto the right swingarm.
4. For 2015+ models, place the ABS rear wheel speed sensor on the inside of the rear brake caliper holder.

   Route the wire feeding the speed sensor around the caliper holder bracket and ensure that the sensor and wire will install without tension or excessive bending.
5. Roll the wheel into position inside of the axle.

   Ensure the speed sensor on the right side mates with and covers the rear wheel bearing before it aligns with the rear brake caliper holder on the right side, as this "sandwiches" together.

   Ensure that the brake calipers are pushed to maximum expansion, then place them around the rear wheel brake disc on the right side.
6. Push the axle through the wheel by hand or use a rubber mallet to gently nudge the axle through the wheel.

   You may need to give the wheel a wedge underneath to rest on to minimize any stress on the axle while aligning it fully.
7. Align the right side of the wheel with the swingarm axle hole and brake caliper holder on the right side.
8. Again, manually push or nudge with a rubber mallet the axle through the speed sensor, rear brake caliper holder, and right swingarm.
9. Run the belt over the rear sprocket.

   Center the belt over the sprocket so it has about 1mm on either side.
10. Ensure that all components are aligned correctly before attempting to tighten the axle or even before mating the left axle end with the swingarm (which tightens the belt).
11. Place the axle nut onto the right side of the axle by hand.
12. Note the alignment of the left and of the axle's rectangular tabs; hold it in a horizontally aligned position so that tightening the axle nut places it inline with the swingarm slot.
13. Tighten the axle nut (27mm) with the torque wrench to 75ft-lbs.

    Ensure the alignment of the axle head on the left side is horizontal and pulls the belt under tension smoothly.

    Check belt tension per the [belt adjustment procedure](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belt_Adjustment).

#### [Rear Bearings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Bearings)

The [rear wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel) contains 3 bearings and dust shields.

| Years | Platform | Kind | Type Code | Measurements | Lifespan (guide) |
| --- | --- | --- | --- | --- | --- |
| 2012-2014 | S | Unsealed | 6904-2RS | 20x37x9 | ~20,000 miles |
| 〃 | X | 〃 | 6204 | 20x47x14 | 〃 |
| 2015-2020 | SDS | Sealed | NSK 6204DU |  | ~50,000 miles |
| 〃 | XMX | 〃 |  |  | 〃 |
| 2020- | FST | 〃 |  |  |  |

**References**

[Precision bearings & replacement](http://electricmotorcycleforum.com/boards/index.php?topic=6692).

[Anyone know front wheel bearing size](http://electricmotorcycleforum.com/boards/index.php?topic=4967).

[Ceramic bearings](http://electricmotorcycleforum.com/boards/index.php?topic=5612) for a 2014SR, with success reported for at least as long as the original bearings. The author is going back to steel.

**Per Terry Hershner**

The 2012-2014 wheel bearings are 6904 bearings which are bicycle sized bearings.

They lasted me about 20,000 miles per set.

Best is to use a 2015 wheel on the 2014 which will work but requires modification of the spacers.

I did it on my 2012. It now has 2015 wheels.

#### [Rear Bearings Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Bearings_Replacement)

**[Rayivers on Wheel bearing replacement ('14 FX, 6904 bearings)](http://electricmotorcycleforum.com/boards/index.php?topic=6692.0)**

Removal was pretty straightforward with a Motion Pro blind bearing removal kit.

Pullers like these are the only way I know of to remove wheel bearings without risk of damage to the hub or center spacer

They pull against the small chamfer on the inner-race I.D.

![Rear Wheel - Left Side - Bearing Disassembly.jpg](../images/Rear_Wheel_-_Left_Side_-_Bearing_Disassembly.jpg)
![Rear Wheel - Right Side - Bearing Disassembly.jpg](../images/Rear_Wheel_-_Right_Side_-_Bearing_Disassembly.jpg)

**Greg Hassler reports**

"I use my brake caliper piston puller, 20mm size works great." <https://www.klsupply.com/general-equipment/brake-caliper-pist-puller-set-35-6885.asp>

**Togo found this tool to work well for 6904-2RS on 2014 Zero SR**

<https://smile.amazon.com/Wheels-Manufacturing-Sealed-Bearing-Extractor/dp/B00NIPRNA4/>

**See Also**

- [Rear Wheel Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel_Removal)
- [Rear Wheel Install](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel_Install)

## Suspension

### Front Suspension

Zero's motorcycles all feature [telescoping fork](https://en.wikipedia.org/wiki/Telescopic_fork) front suspension.

#### [Front Suspension Specs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Suspension_Specifications)

|  |  | Fork |  |  |  |  |  |  | Shock |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Years | Manufacturer | Description | Material | Model | Part# | Travel | Measurements | Oil | Material | Part# | Measurements |
| 2009-2010 | [FastAce](http://www.fastace.com/) |  |  | DS/X |  |  |  |  |  | BDA53AR ([discontinued](http://www.fastace.com/pro.php?m=sh&keyword=BDA)) |  |
| 2012-2013 | 〃 | 38mm (from Zero website/manual) inverted forks with adjustable compression and rebound damping | [6061-T6](https://en.wikipedia.org/wiki/6061_aluminium_alloy#6061-T6) Forged Aluminum (per [this thread](http://electricmotorcycleforum.com/boards/index.php?topic=3288.msg17395#msg17395)) <br> Chrome-Moly inner tube; Alloy steel spring wire | S | ALX07RC ([discontinued](http://www.fastace.com/pro.php?m=sh&keyword=ALX)) 22-05418-03 <br> **Right** <br> 22-04464-05 <br> **Left** <br> 22-04463-05 | 140mm | Compression 12 clicks; Rebound 21 clicks |  | [6061-T6](https://en.wikipedia.org/wiki/6061_aluminium_alloy#6061-T6) Forged Aluminum (per [this thread](http://electricmotorcycleforum.com/boards/index.php?topic=3288.msg17395#msg17395)) | BDA58RC ([discontinued](http://www.fastace.com/pro.php?m=sh&keyword=BDA)) |  |
| 〃 | 〃 | 〃 | 〃 | DS | **Left** <br> 22-06093-02? <br> **Right** <br> 22-06094-02? <br> (APX05RC? or APX10AR? ([discontinued](http://www.fastace.com/pro.php?m=sh&keyword=APX))) | 7.00 in (178 mm) | clarification? <br> **Distance** <br> 900 mm <br> **Travel** <br> 220 mm |  | 〃 | BFA57RC ([discontinued](http://www.fastace.com/pro.php?m=sh&keyword=BFA))) | **Rebound Adjustment** <br> 12 clicks |
| 〃 | 〃 | 〃 | 〃 | FX/MX/XU | XU - ALX07RC AP18A0179-B002 22-02749-01 | **XU** <br> 51mm (manual) <br> 130mm (website) <br> **MX** <br> 82mm (manual) <br> 240mm (website) <br> **FX** <br> 240mm |  |  | 〃 |  |  |
| 2014 | 〃 | 43 mm inverted forks with adjustable compression and rebound damping | [6061-T6](https://en.wikipedia.org/wiki/6061_aluminium_alloy#6061-T6) Forged Aluminum (per [this thread](http://electricmotorcycleforum.com/boards/index.php?topic=3288.msg17395#msg17395)) <br> Chrome-Moly inner tube; Alloy steel spring wire | S/SR |  | 6.25 in (159 mm) |  |  | [6061-T6](https://en.wikipedia.org/wiki/6061_aluminium_alloy#6061-T6) Forged Aluminum (per [this thread](http://electricmotorcycleforum.com/boards/index.php?topic=3288.msg17395#msg17395)) | BDA58RC ([discontinued](http://www.fastace.com/pro.php?m=sh&keyword=BDA)) |  |
| 〃 | 〃 | 〃 | 〃 | DS | APX16RC - 22-06867-05 <br> **Right** <br> 22-06869-05 <br> **Left** <br> 22-06868-05 | 7.00 in (178 mm) | Compression 11 clicks; Rebound 20 clicks |  | 〃 | BFA57RC ([discontinued](http://www.fastace.com/pro.php?m=sh&keyword=BFA))) | **Rebound Adjustment** <br> 12 clicks |
| 〃 | 〃 | 〃 | 〃 | FX |  | 230mm |  |  | 〃 |  |  |
| 2015-2020 | [Showa](http://www.showa1.com/en/product/motorcycle/shock_absorber_f.html) | 41 mm inverted cartridge forks, with adjustable spring preload, compression and rebound damping | **Outer Tube Finish** <br> Natural Anodized (silver) <br> **Slide Tube Finish** <br> Nickel - Hard Chrome <br> **Rebound (Tension) Finish** <br> Black Anodized <br> **Compression Finish** <br> Black Anodized | S/SR |  | 6.25 in (159 mm) | **Free length** <br> 461.5mm. <br> **Outer diameter** <br> 36.2mm. <br> **Stock spring rate** <br> 7.4 N/mm | **Type** <br> SS-8 <br> **Level** <br> 117 mm | **Body Finish** <br> Natural Anodized (silver) <br> **Rod Finish** <br> Nickel - Hard Chrome <br> **Rebound (Tension) Finish** <br> Black Anodized <br> **Compression Finish** <br> Black Anodized |  |  |
| 〃 | 〃 | 〃 | 〃 | DS/DSR |  | 7.00 in (178 mm) |  |  | 〃 |  |  |
| 〃 | 〃 | 〃 | 〃 | FX | **Left** <br> 22-05868-02 <br> **Right** <br> 22-05869-02 |  | **Free Length** <br> 789.1±2.0mm <br> **Max Length** <br> 798mm <br> **Min Length** <br> 580mm <br> **Stroke** <br> 218mm <br> **Spring Rate** <br> 5.4 N/mm <br> **Rebound (Tension)** <br> Max - 9 clicks <br> **Compression** <br> Max - 5 clicks <br> **Preload** <br> Min + 3.0 turns | **Type** <br> [SS-8](https://transmoto.com.au/comparative-oil-weights-table/) <br> **Volume** <br> 442±2.5cm3 <br> **Level** <br> 103mm | 〃 | 22-05879-02 | **Spring Rate** <br> 73.6-82.4 N/mm <br> **Free Length** <br> 320±2.0mm <br> **Max Length** <br> 320.5mm <br> **Min Length** <br> 246mm <br> **Stroke** <br> 74.5 <br> **Rebound (Tension)** <br> Max - 12 clicks <br> **Compression** <br> Max - 9 clicks <br> **Preload** <br> 2nd Position |
| 〃 | 〃 | 〃 | 〃 | FXS |  |  |  |  | 〃 |  |  |

#### [Fork Oil Change and Spring Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Fork_Oil_Change_and_Spring_Replacement)

**Fork Oil Level Note**

Measure from outer tube end to oil surface (Condition: spring, spring joint, spring collar, seat rubber, slider, fork bolt are removed and dust seal touches axle holder)

**Reference**

[FastAce fork oil change / spring replacement](http://electricmotorcycleforum.com/boards/index.php?topic=4929)+ [part 2](http://electricmotorcycleforum.com/boards/index.php?topic=5323) by Ray Ivers

**Tools**

- 7mm Allen wrench for riser bolts.

**Steps**

1. Put the motorcycle on a stand.
2. Remove the risers and handlebars using a 7mm Allen wrench.
3. Loosen the fork caps, front axle, and brake caliper bolts while the front wheel is on the ground.
4. Fork cap / spring removal...
5. Oil change...
6. Fork spring / cap replacement...

**Notes**

| What | Torque | Bolt |
| --- | --- | --- |
| Handlebar clamps | 15 ft/lb | M8 |
| Handlebar risers | 25 ft/lb | M10 |
| Triple clamps (all) | 15 ft/lb | M8 |
| Fork caps | 15 ft/lb | M46 |
| F caliper bolts | 18 ft/lb | M8 |
| F axle end cap | 15 ft/lb | M8 |
| F Axle clamps | 9 ft/lb | M6 |

#### Fork Cartridge Revalving

[Fast Ace fork revalving](http://electricmotorcycleforum.com/boards/index.php?topic=7737) by Ray Ivers

The procedure is described in great detail for FastAce (2013-2014) suspension but could be adapted for the newer Showa suspension.

#### [Verify Fork Spring Rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Fork_Spring_Rate_Verification)

**Reference**

[How to Verify Fork Spring Rate](http://electricmotorcycleforum.com/boards/index.php?topic=5320.msg39353#msg39353)

**Tools**

- A tip-tie long enough to wrap around the fork tube.

**Steps**

1. Add a zip-tie to the the fork tube.
   - Make sure it is snug so it stays in the place it was last pushed too.
   - Once the zip-tie is on the fork tube, you push it up to rest it against the upper fork.
2. Measure *bike sag* (unloaded)

   Lift the front fork off the ground and measure the gap (zip-tie to fork gap) created by the front weight of the bike.
3. Measure *rider sag* (loaded)
   1. Now push zip-tie back up the fork, then sit on the bike and raise your feet so all of your weight is carried through the suspension.
   2. Then carefully dismount and put kickstand down.
   3. Measure the gap (zip-tie to fork) created by your weight.
   4. Add this gap measurement to the *bike sag* measurement, this is the *total sag*.

   This measurement should be around 25% of the working range of the front suspension.

   Now that is a guideline; it can be higher or lower than 25%.

   It depends on what is happening when you are loading up the suspension (upper end).
4. Checking the upper end by using the zip-tie.

   After riding, check the location of the zip-tie: the gap from the fork to the zip-tie.

   Lets say the measurement is 5". Then you would know the total max travel used was 5" + *bike sag* measurement.

That total measurement should never equal the total suspension travel amount (6", I think based on your posting).

- If it equal, then you are bottoming out. Increase the preload and see if this keeps you from bottoming out.
- If you use max preload and are still bottoming out, you will need stronger springs.
- If you find you are only using 75% to 80% of the max suspension travel, you can reduce the preload spacer length some or you can live with this.
- If you are only using ~50% or less of the suspension travel, your springs are probably too stiff. You should swap springs to a lower rate spring.

### [Rear Shock](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Shock)

Zero motorcycle models use a [single shock absorber](https://en.wikipedia.org/wiki/Motorcycle_suspension#Single_shock_absorber) rear suspension, joining the [Swingarm](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Swingarm) to the [Frame](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Frame).

#### Rear Shock Mounting

The rear shock fastens to the [Swingarm](#Swingarm) by an M10 bolt.

The upper mount reaches the frame centertube ahead of the [controller heatsink](#Controller_Heatsink) area so is difficult to access.

#### [Rear Shock Specifications](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Shock_Specifications)

| Years | Brand | Model | Description | Media | Specs | Models | Travel | Length |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2013-2014 | [FastAce](http://fastace.com/index_moto.html) | BDA58RC | Piggy-back reservoir shock with adjustable spring preload, compression and rebound damping | ![2013 S Rear Shock FastAce BDA58RC](../images/2013_Zero_S_Rear_Shock_FastAce_BDA58RC.jpg) *2013 S Rear Shock FastAce BDA58RC* | **Spring Rate** <br> 550 ~ 805 lbs/in <br> **Spring** <br> Length 142mm, Diameter 57mm <br> **Bottom bushing width** <br> 11/16" <br> **Top bushing width** <br> ~1.25" | S/SR | 6.35 in (161 mm) | 10.25-10.5 in (260mm) |
| 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | DS | 7.03 in (179 mm) |  |
| 〃 | 〃 | BFA57RC <br> Part 22-06105-03 | 〃 |  | - 319mm / 12.56" eye-eye <br> - 17.9mm / .705" eye width (top & bottom) <br> - 31.95mm / 1.258" bushing width (top & bottom) <br> **Resevoir** <br> offset angle ('clocking angle'): 242° CW / 118° CCW from 12 o'clock <br> offset width (shock centerline to far LH side of reservoir): @ 90mm / 3.60" <br> **Spring Rate** <br> 475-585 lbs/in. <br> **Spring** <br> 181mm / 7.125" length (on shock, no load, min. preload) | FX |  |  |
| 2015-2020 | [Showa](http://www.showa1.com/en/product/motorcycle/shock_absorber_r.html) |  | 40 mm piston, piggy-back reservoir shock with adjustable spring preload, compression and rebound damping |  |  | S/SR | 6.35 in (161 mm) |  |
| 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | DS/DSR | 7.03 in (179 mm) |  |

#### [Rear Shock Substitions](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Shock_Substitutions)

| Years | Models | Worked? | Description |
| --- | --- | --- | --- |
| 2013-2014 | S/SR | Yes | [JRI Double-Adjustable Shocks](https://www.jrishocks.com/shop/powersports/double-adjustable/) per [2014 SR shock absorber replacement by Doug S](http://electricmotorcycleforum.com/boards/index.php?topic=6936) with Harlan's help. |
| 〃 | 〃 | Yes (with machining) | Wotefusi [[1]](https://www.amazon.com/Wotefusi-Motorcycle-Absorber-Replacement-Universal/dp/B01A8HWKNE/ref=sr_1_16?ie=UTF8&qid=1516726305&sr=8-16&keywords=260mm+shock) 260mm Central Air Shock Absorber Universal Fit - fits when mounted upside down. Need to cut/grind down the bushing. |
| 〃 | 〃 | Yes (with machining) | TDPRO 260mm 10.2 [[2]](https://www.amazon.com/gp/product/B01M0DE754/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1) Almost fits; the area on top of the spring is just slightly too large. You can take a grinder and shave away some of the top to make it fit. [[3]](http://electricmotorcycleforum.com/boards/index.php?topic=7753.0) |
| 〃 | 〃 | NO | The Yamaha R3 has the same length rear shock, but the spring is too wide. |
| 〃 | 〃 | NO | Fastace Rear Shock BDA-51AR/58-AR has a weaker spring, and is rotated 90 degrees. [[4]](https://www.amazon.com/gp/product/B01B3Q2O8A/) |
| 〃 | 〃 | Mixed results - new orders may have all the kinks worked out. | IKON 3610-ZERO-S Shock Absorber [[5]](https://www.ikonshocksusa.com/products/3610-zero-s-shock-absorber?variant=28622432206908) - The spring is too wide at the top, and to be installed, the sping must be compressed. When Installation is complete, the spring is always compressed by at least a couple centimeters. |
| 〃 | 〃 | Mixed results - Get dimensions from Wilber's dealer before ordering - theirs is ~279mm | Wilbers Shock absorber Type 640 Road Part. No.: 640-1143-00 [[6]](https://www.wilbers-shop.de/en/Motorcycle/Zero-Motorcycles/Zero-S-Z1-M5/Shock-absorber-Type-640-Road.html?year=2014) Wilbers claims the shock fits "2011-2013 S M5" (which does not exist). The M5 designation is buried in the VIN of the 2014 S; and may or may not be relevant. This shock could be mislabeled for the DS. Make sure to get full dimensions before ordering. |
| 〃 | 〃 | Yes - DO NOT BUY | ZXTDR Rear Shock Absorber Suspension Sensa-Trac Load Adjusting for Dirt Pit Bike Motorcycle 1200LBS. [[7]](https://www.amazon.com/gp/product/B074J3X2P5/) This shock phyisically fits, but underperforms. It feels like you're riding on a trampoline. You get what you pay for. |

#### [Rear Shock Adjustment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Shock_Adjustment)

**Notes**

The [Official Manual](Official_Owners_Manual.md "Official Owners Manual") section on Rear Shock Adjustment illustrates how to measure preload and check sag.

**Compression**

The official manual's description here is adequate and this can be done readily by hand on the right side of the bike at the top of the shock.

**Rebound**

The adjustment knob is at the bottom of the shock facing rear, as described in the manual, and can be worked by hand or with a wrench with a careful reach into that area.

**Spring Preload**

The official manual illustrates the collar and procedure for spring preload adjustment, but does not recommend a specific tool, and there are clearance issues in that area for tools.

The adjuster sleeve diameter is 58mm (2.3").

A Stockton spanner wrench was found to be suitable for the job if modified as follows (per [2017 DSR Showa rear shock spanner wrench](http://electricmotorcycleforum.com/boards/index.php?topic=6674.msg53551#msg53551)):

- Grind the nose of the wrench to fit the notches.
- Bend the wrench a couple of degrees to clear the Sevcon motor controller fins.

Obviously, a better solution is still worth seeking.

A small suspension wrench / ER collet spanner size 30/32 can be use even with the lack of clearance

![Suspension wrench around the collar](../images/20180502_172307.jpg) *Suspension wrench around the collar*

## Final Drive

### [Swingarm](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Swingarm)

The swingarm is a dual-sided structure made in the same way as the [frame](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Frame). It's very sturdily constructed for its light weight.

![Swingarm](../images/Onlift.jpeg) *Swingarm*

The front pivots on the axis of the [motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor) to minimize [belt](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt) strain with suspension travel.

It has fitments for the [rear axle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Axle) including belt tension adjustment.

**Mounting**

The swingarm joins the frame at left and right pivot points.

The each side pivot has a stack of (from outside inward):

- A rubber cover
- A bolt with a 10mm hex drive.
- The bearing (6204; 6204RS for 2015+ models)

#### [Swingarm Tube](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Swingarm_Tube)

There is a hollow tube through the [swingarm](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Swingarm) across the arms forming a join point for the [rear shock](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Shock) to the [frame tube](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Frame_Tube) on the SDS platform.

![Swingarm Tube with measurements](../images/2018-sr-swingarm-hole.png) *Swingarm Tube with measurements*

Its shape is flattened on the rear side, presumably to clear the largest-diameter potential tire.

It makes a reasonable storage tube *if* some padding or caps are used to secure the cargo there (like a charging cord).

| | | |
| --- | --- | --- |
| Inner diameter | 75mm | 2.91" |
| Horizontal width to flat side | 68mm | 2.68" |
| Swingarm greatest width below tube | 295mm | 11.61" |

**References**

[Re: Through-frame security aperture size?](http://electricmotorcycleforum.com/boards/index.php?topic=8163.msg68924#msg68924)

#### [Swingarm Bearings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Swingarm_Bearings)

The swingarm bearings are generally the same as the [wheel bearings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Bearings) (6204; 6204RS for 2015+ models).

#### [Swingarm Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Swingarm_Removal)

**Tools**

- [Center lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) or other lift that gets the rear wheel off the ground without contacting the swingarm.
- 27mm socket or spanner.
- 3mm Allen key.
- 10mm Allen key socket

  Ensure at least 1" depth and a ⅜" drive sufficient to handle swingarm pivot bolt torques.
- 15mm socket wrench (S models).
- 13mm socket wrench (X models).
- Torque wrench capable of setting 75ft-lbs and driving the 27mm socket and 10mm Allen key.
- 2012-2013:
  - 2.5mm Allen key.
  - 24mm socket wrench.

**Steps**

**NOTE:** For roadside removal, particularly for an FX or FXS, setting the bike on its side should be possible for this work.

However, no effective procedure has been described for the process.

The following steps are suited to garage locations.

![Bike on center lift](../images/Onlift.jpeg) *Bike on center lift*

1. Use a [lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) to raise the bike from the center.

   A sturdy wood crate may work in a pinch. Be safe.

   If the lift can be adjusted, lift the rear wheel just off the ground for ease of removal and replacement (lower than depicted but not in contact).
2. Pull the wheel off (or slide it forward) by loosening the axle nut with a 27mm wrench.
3. Pull off the rear tire fender by taking out the 4 hex bolts securing it with a 3mm Allen wrench.

   You can get away with removing only the left-side screws, to allow lifting the fender up enough to get the belt under.

   The right side fasteners also anchor the brake line to the rear calipers and a grounding strap, so mind them for re-attaching in the same way.
4. Remove the brake pedal:

   This creates clearance for loosening the swingarm bolt above it *(might be optional for pre-2015 models)*.
5. Get the rear brake pedal out of the way of the right side swingarm pivot bolt.

   **SDS platform:** Use the 15mm hex socket to loosen or remove the bolt forming the pedal pivot.

   **XMX platform:**
   1. Remove the pin that attaches the brake pedal to the piston.
   2. Remove the two 13mm bolts that hold the grey piston bracket to the frame, and gently move the whole assembly to the left.

   ![Rear Brake Lever Bolt](../images/Rearbrakebolt.jpeg) *Rear Brake Lever Bolt*
6. **XMX platform:** To access the left swingarm bolt, remove the lower left passenger peg bolt (13mm) and remove the grey cover piece.
7. Remove the left and right swingarm bolts.

   **2012-2013**

   Remove the set screws from the swingarm bolts on both sides with a 2.5mm Allen wrench.

   The set screw is very difficult to find.

   It is located in one of the sides of the 24mm hex nut, perpendicular to the long axis of the 10mm allen bolts.

   It is actually on the edge of the nut.

   The best way to locate it is to use a small mirror and a strong flashlight.

   Then remove the bolts by holding the inside nut with a 24mm wrench, and a 10mm hex on the head.

   This was the hardest step, because there is not a lot of room to manipulate in the rear assembly - especially with a 24mm wrench!

   **2014+**

   Remove the left and right swing arm bolts with a 10mm Allen wrench.

   ![Swingarm Bolt](../images/Swingarmbolt.jpeg) *Swingarm Bolt*
8. Hang the swing arm with a strap on the tail section.

   The swingarm will pull back enough for the belt to fit through the frame.

   ![Pulling the Swingarm](../images/Swingarmpull.jpeg) *Pulling the Swingarm*

   ![Swingarm Pulled](../images/Swingarmpulled.jpeg) *Swingarm Pulled*
9. Remove the belt.
10. Disconnect the rear shock from the swingarm, then gently pull the swingarm from its suspended arrangement. Take car that the small spacers do not fall out and roll away, one on each side.

**References**

[Swingarm Bolt Set Screw?](http://electricmotorcycleforum.com/boards/index.php?topic=8184)

### [Rear Axle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Axle)

The rear axle is hollow, threaded on the right side and capped on the left for swingarm fitment.

| Years | Inner Diameter | Outer Diameter | Pitch |
| --- | --- | --- | --- |
| 2013-2014 |  |  |  |
| 2015+ | 11mm | 20mm | 1.25mm |

#### [Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Axle_Removal)

This removes the [Rear Axle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Axle) part of [Rear Wheel Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Wheel_Removal).

**Tools**

- 27mm socket
- Breaker bar

**Instructions**

1. Place the motorcycle on a [lift or rear stand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift)

   Raise just enough that the rear wheel spins freely.
2. Mark/photograph where the alignment marks reside on each side of the axle for re-alignment when re-installing the wheel.
3. On the right side, loosen the rear axle nut (27mm) with the breaker bar.
4. Remove the rear axle nut.
5. Pull the axle part-way out so that the wheel can be moved forward enough to loosen the belt.
6. Pull the belt off of the rear sprocket.

   Let it hang outside of the swingarm slightly to avoid interfering with the wheel.
7. From the left side, pull the axle through the wheel.

#### [Install](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Axle_Install)

To replace the [rear axle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Axle), see [rear wheel replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel_Install).

### [Belt](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt)

Zero uses a belt for primary transmission of torque to the rear wheel. It's quiet and lightweight but is a proprietary design that can wear out. If you plan to put a lot of miles on a Zero or risk the belt often, buy a spare belt ahead of time and mind its maintenance.

#### [Belt Risks](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt/Risks)

Drive belts fail by snapping or by stripping the teeth.

**On Landing**

The most common situation for a belt snap is when going over a major bump or jump where the rear wheel leaves the ground.

- If, while airborne, the throttle is not immediately relaxed, the rear wheel will rapidly spin up.
- A wheel that is moving extremely quickly in the air will get jerked back to its regular speed on landing. This is transmitted to the belt through the rear sprocket and can easily strip teeth.

**From Debris**

Gravel or sand that gets thrown between sprocket teeth and the belt will force the belt to expand quickly under load, and can cause it to snap.

Reportedly, sand is a much more reliable path to belt failure than gravel.

The sprocket tooth design is meant to deflect gravel to the inside of the swingarm towards the wheel.

The bike has an upper debris guard made of soft ABS plastic, but does not have a lower guard.

**From Mis-Alignment**

An unaligned belt can wear really badly and break sooner.

#### [Belt Specifications](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt/Specifications)

Zero's final drive is a custom-designed [Gates](http://www.gates.com/) [HTD (high torque drive)](http://www.gates.com/products/industrial/industrial-belts/synchronous-belts/powergrip-htd-belts) [Poly Chain Carbon](http://www.gates.com/products/industrial/industrial-belts/synchronous-belts/poly-chain-htd-belts) toothed carbon fiber belt.

- It's never been available outside of Zero's parts system.
- It's been the same part for 2012-2016 models.

  2017 models shifted to a wider belt that can accommodate more torque/loading.

| Years | Width | Pitch | Models | Sprockets | Number of Teeth | Length | OEM Part No. | Photo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [2010-2011](http://electricmotorcycleforum.com/boards/index.php?topic=7439.0) | 14mm | 8mm | S/DS | 98T / 28T | 200 |  | 30-02641 |  |
| 2012-2016 | 〃 | 〃 | S/SR | 132T / 28T | 220 |  | 30-03673 (old logo) <br> 30-08084 (new logo) | ![reference photo of belt](../images/ZM30-08084.png) |
| 〃 | 〃 | 〃 | DS/DSR | 130T / 28T | 〃 | 〃 | 〃 | 〃 |
| 2017- | 17mm | 14mm | S 13.0 | 130T / 28T | 〃 | 〃 | 〃 | 〃 |
| 〃 | 〃 | 〃 | FX/FXS <br> DS/DSR <br> SR/S6.5 | 90T / 20T | 158 |  | 30-08086 | ![reference photo of wide belt](../images/ZM30-08086.png) |
| 2020- | 20 | 11 | SRF | 90T / 20T | 151 |  | 30-08226 |  |

**Part**

[Gates GT Carbon, 14mm wide, 8mm pitch, 220 teeth](http://electricmotorcycleforum.com/boards/index.php?topic=5846). It's only available from Zero.

P/N's are 30-03673 ("Belt Drive, 220T, 8mm Pitch, 14mm Wide") and also 30-08084 (same belt w/new Zero logo).

One rough match for reference: [Gates 8MGT-1760-12 Belt](http://www.biedlers-belts.com/gates-8mgt-1760-12-belt.html)

Another Gates product page that highly indicates a product/technology match: [Poly Chain® GT® Carbon™ synchronous belts](https://www.gates.com/us/en/power-transmission/synchronous-belts/poly-chain-synchronous-belts/poly-chain-gt-carbon-belts/p/9268-000000-000045) per [Gates drive belts (EMF Thread)](https://www.electricmotorcycleforum.com/boards/index.php?topic=9702)

#### [Belt Tension Check](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt/Tension_Check)

**Krikit Tension Gauge**

Zero recommends the [Gates Krikit belt tension gauge](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_4&products_id=191) to check belt tension.

![Krikit Tension Gauge invoice and box](../images/GATESKRIKITIVBELTTENSIONGAUGE10-04627_invoiceandbox.jpg) *Krikit Tension Gauge invoice and box*

![Krikit Tension Gauge gauge and instructions](../images/GATESKRIKITIVBELTTENSIONGAUGE10-04627_gaugeandinstructions.jpg) *Krikit Tension Gauge gauge and instructions*

**Video Guide**

MostlyBonkers made a [How-to video](https://www.youtube.com/watch?v=aifDR4jWG0E):

**Tips**

- Turning the back wheel backwards before measuring will give different readout compared to turning the wheel forwards before measuring using the same spot.

  The difference may be significant to the (pre-2017) 20-30kg belt tension specification.

  For wide-belt 2017+ models, the tension specification is very wide (~25-75kg) and thus has a lot of leeway but seems worth a rotational check anyway.
- The center of the belt can be reached from below, without removing the mudguard.

  This is described as a note in 5.14 in the 2015 manual

**Steps**

[More detailed generic instructions for the Krikit deflection device](http://www.newenglandbelting.com/bt_method3.asp)

1. Ensure the blue indicator arm is pressed down.
2. Place the gauge in the center of the belt span, such that it is aligned longitudinally with the belt length.
3. Place a finger on the blue pressure pad and depress this pressure pad.
4. Keep pressing the blue pressure pad until you feel and hear a distinct 'click'. When this 'click' sound is heard, do not press any further.
5. Remove the gauge and read the belt tension by observing the point where the top side of the blue indicator arm crosses the numbered scale on the gauge body.

- Care must be taken to ensure that the gauge is not 'rocked' when pressing down on the blue pressure pad. The strap above the pressure bar is provided to attach snugly over the finger and prevent any 'rocking' motion.
- Due to the fact that this device requires some amount of practice and operator skill, the accuracy and repeatability of the tension readings are not high.

**Improvement**

Because this procedure is not trivial to perform consistently, there is a modification to [make the tension gauge easier to align](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Zero_Aftermarket)

**Gates' Carbon Drive mobile app**

As of 2017, the [Official Owners Manual](Official_Owners_Manual.md "Official Owners Manual") also includes a procedure using [Gates' Carbon Drive mobile app](http://www.gatescarbondrive.com/products/tools) to check belt tension.

- [iOS version](https://itunes.apple.com/us/app/carbon-drive-bicycle-calculator/id438346486?mt=8)
- [Android version](https://play.google.com/store/apps/details?id=com.gates.carbondrivecalculator&hl=en)

**Usage**

- Use the application in a quiet environment.
- Pluck the belt near the center of the lower belt span, so it vibrates like a guitar string.

| Belt Type | Years | Resonant Frequency | Tension Range |
| --- | --- | --- | --- |
| Narrow | 2013-2016 | 96.3 Hz – 124 Hz | 20 – 30kg |
| Wide | 2017+ (except S 13.0) | 42.5 Hz – 73.6 Hz | 25 – 76.5kg |

The frequency can also be checked with instrument tuning apps such as [Tuner-gStrings](https://play.google.com/store/apps/details?id=org.cohortor.gstrings) for Android.

#### [Belt Adjustment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Drive_Belt_Adjustment)

**Goal**

Align and set belt tension to avoid bad wear and early breakage.

Alignment of the belt is critically tough to get correct, and needs to be done everytime adjusting tension.

Zero's [Official Owners Manual](Official_Owners_Manual.md "Official Owners Manual") has a good procedure from which this is derived. Check that first.

**Video instruction**

[Zero SR: How To Adjust Your Belt](https://www.youtube.com/watch?v=mab3a7MWrpY) on Youtube by NewZeroLand:

**Tools**

27mm hex socket

Breaker bar

Torque wrench set to 75ft/lbs or 102Nm

13mm open-end wrench

**Instructions**

1. Place the motorcycle on a [Lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) or rear stand so the wheel spins freely.
2. Loosen the rear axle nut on the right side (27mm) with the breaker bar.

   ![Rear Axle Nut and right adjustment bolt](../images/Rear_Axle_Nut_and_right_adjustment_bolt.jpeg) ![Rear Axle Spacer and left adjustment bolt](../images/Rear_Axle_Spacer_and_left_adjustment_bolt.jpeg)
3. Loosen both left and right belt tension jam nuts (13mm) that face forward inside the adjusting gap.

   ![Rear Axle Nut and right adjustment bolt - loosened](../images/Rear_Axle_Nut_and_right_adjustment_bolt_-_loosened.jpeg) ![Rear Axle Spacer and left adjustment bolt - loosened](../images/Rear_Axle_Spacer_and_left_adjustment_bolt_-_loosened.jpeg)
4. Turn both left and right adjustment nuts (13mm) one quarter turn at a time to the desired [belt tension](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt/Tension_Check).
   - Ensure that the alignment marks on either side of the swingarm indicate that the wheel and belt are aligned.
   - Roll the wheel forward and track it flush with inside of rear sprocket.
   - For proper alignment, the belt will track exactly centered on the wheel sprocket with a 1mm gap to either side of the belt relative to the sprocket.

     Once tension is set and tracking is flush to the inside, tightening the axle nut to 75ft-lbs will tend to nudge belt approximately 1mm to the outside.
   - Measure tension by rolling the wheel forward while plucking bottom side of belt or using tension gauge over several revolutions.

     Expect tension to vary slightly as wheel is rotated because front and rear sprockets are only round to a certain design tolerance.
5. Check that the belt is aligned with belt tension in the right range.
6. Re-tighten the left and right jam nuts (13mm).
7. Tighten the axle nut (27mm) with the torque wrench (to 75ft-lbs).

**References**

[Belt alignment discussion](http://electricmotorcycleforum.com/boards/index.php?topic=3813)

[How to Adjust Your Zero's Belt](http://electricmotorcycleforum.com/boards/index.php?topic=6921)

[Notes via Shadow](http://electricmotorcycleforum.com/boards/index.php?topic=6921.msg56601#msg56601)

#### [Belt Wear](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt/Wear)

Generally, watch for belt damage and try to anticipate when to replace the belt to avoid an incident on the road where the belt snaps.

**What to Check**

- Check the teeth for wear and cracks.

  If you see cracks in the tooth forming, the belt is getting old.

  If you see deep cracks starting, it's time to [replace the belt](#Belt_Replacement) ASAP.

  ![Rear Drive Belt Wear Analysis](../images/Rear-drive-belt-wear-analysis.jpeg) *Rear Drive Belt Wear Analysis*

**When to Replace**

- When it snaps.
- When any teeth have been ground off.

**Hard Skips**

- If the belt experiences a "hard skip" from debris between the belt and a sprocket, it is likely to fail soon after. Watch it carefully if this happens.

**Tension with aging**

Apparently, [per forum user JaimeC](http://electricmotorcycleforum.com/boards/index.php?topic=5693.msg42069#msg42069), belts don't wear like chains.

As they get older they'll actually get tighter, not looser like a chain.

- When a chain ages, the little bearing points between the links and rollers wear causing the chain to hang looser.
- When a belt ages, the rubber on the inner/toothed side begins to swell.

Since the Kevlar belt on the outer circumference won't stretch, the inner circumference will shrink making the belt tighter around the sprockets.

Generally, you want to make sure the belt hasn't gotten any tighter since you brought it home.

**References**

- [Drive Belts](https://www.electricmotorcycleforum.com/boards/index.php?topic=10293)

#### [Belt Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Drive_Belt_Replacement_Procedure)

Ask your dealer/Zero before replacing it.

They may perform it under warrantee if it happened prematurely; and they'll likely want to understand how and why it broke, anyway, for quality reasons.

**Video Guides**

- [How To: Replace Your Zero Motorcycle Belt](https://www.youtube.com/watch?v=zGi19IYRnrc) by [NewZeroLand](https://www.youtube.com/channel/UCdEMqkiM5I-98gxZKJXQ65Q) on YouTube:
- [Zero emergency toothed belt](https://www.youtube.com/watch?v=9o0qhMdAKDc) by [UW4E](https://www.youtube.com/channel/UC6z8t3aHDKTDYJbW6_pSqsA) on YouTube:

**Tools**

- [Center lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift).
- 27mm socket.
- 3mm Allen key.
- 10mm Allen key socket

  Ensure at least 1" depth and a ⅜" drive sufficient to handle swingarm pivot bolt torques.
- 15mm socket wrench (S models).
- 13mm socket wrench (X models).
- Torque wrench capable of setting 75ft-lbs and driving the 27mm socket and 10mm Allen key.
- 2012-2013:
  - 2.5mm Allen key.
  - 24mm socket wrench.

**Procedure**

**NOTE:** For roadside belt swaps, particularly for an FX or FXS, setting the bike on its side should be possible for this work.

However, no effective procedure has been described for the process.

The following steps are suited to garage locations.

![Bike on center lift](../images/Onlift.jpeg) *Bike on center lift*

1. Use a [Lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift) to raise the bike from the center.

   A sturdy wood crate may work in a pinch. Be safe.

   If the lift can be adjusted, lift the rear wheel just off the ground for ease of removal and replacement (lower than depicted but not in contact).
2. Pull the wheel off (or slide it forward) by loosening the axle nut with a 27mm wrench.
3. Pull off the rear tire fender by taking out the 4 hex bolts securing it with a 3mm Allen wrench.

   You can get away with removing only the left-side screws, to allow lifting the fender up enough to get the belt under.

   The right side fasteners also anchor the brake line to the rear calipers and a grounding strap, so mind them for re-attaching in the same way.
4. Remove the brake pedal:

   This creates clearance for loosening the swingarm bolt above it *(might be optional for pre-2015 models)*.
5. Get the rear brake pedal out of the way of the right side swingarm pivot bolt.

   **S platform:** Use the 15mm hex socket to loosen or remove the bolt forming the pedal pivot.

   **X platform:**
   1. Remove the pin that attaches the brake pedal to the piston.
   2. Remove the two 13mm bolts that hold the grey piston bracket to the frame, and gently move the whole assembly to the left.

   ![Rear Brake Lever Bolt](../images/Rearbrakebolt.jpeg) *Rear Brake Lever Bolt*
6. **X platform:** To access the left swingarm bolt, remove the lower left passenger peg bolt (13mm) and remove the grey cover piece.
7. Remove the left and right swingarm bolts.

   **2012-2013**

   Remove the set screws from the swingarm bolts on both sides with a 2.5mm Allen wrench.

   The set screw is very difficult to find.

   It is located in one of the sides of the 24mm hex nut, perpendicular to the long axis of the 10mm allen bolts.

   It is actually on the edge of the nut.

   The best way to locate it is to use a small mirror and a strong flashlight.

   Then remove the bolts by holding the inside nut with a 24mm wrench, and a 10mm hex on the head.

   This was the hardest step, because there is not a lot of room to manipulate in the rear assembly - especially with a 24mm wrench!

   **XU-2013**

   sane as above, but needed a 23mm wrench and a 2mm Allen wrench instead of the 24mm wrench and 2.5mm allen wrench

   **2014+**

   Remove the left and right swing arm bolts with a 10mm Allen wrench.

   ![Swingarm Bolt](../images/Swingarmbolt.jpeg) *Swingarm Bolt*
8. Hang the swing arm with a strap on the tail section.

   The swingarm will pull back enough for the belt to fit through the frame.

   ![Pulling the Swingarm](../images/Swingarmpull.jpeg) *Pulling the Swingarm*

   ![Swingarm Pulled](../images/Swingarmpulled.jpeg) *Swingarm Pulled*
9. Check the front sprocket for debris, and clean it with a firm but non-abrasive brush.

   If the sprocket is damaged somehow or the teeth are too worn to engage the belt, get it replaced to avoid damaging the new belt.

   The rear sprocket regularly deserves the same treatment.
10. Slide the belt over the front sprocket.
11. Replace the swingarm bolts.
12. Slide the belt over the rear sprocket.
13. [Set/adjust belt tension and alignment accordingly](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Drive_Belt_Adjustment).
14. [Install the rear wheel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Wheel_Install)
15. Re-check belt tension and alignment.
16. Re-install the rear brake pedal.
17. Re-install the rear tire fender.
18. Extend the sidestand, then lower the bike carefully from the lift onto the sidestand.

**References**

[2013 S Belt Replacement](http://electricmotorcycleforum.com/boards/index.php?topic=3530)

[2012 DS Belt Replacement](http://electricmotorcycleforum.com/boards/index.php?topic=3217), by User:DoctorBass

[Swingarm Bolt Set Screw?](http://electricmotorcycleforum.com/boards/index.php?topic=8184)

Facebook comments by Bobby Loo.

### Sprocket

#### [Sprocket Specifications](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Sprocket_Specifications)

| Belt |  |  |  | Front |  |  |  | Rear |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Width | Pitch | Years | Models | Teeth | Depth | Bore | Other | Teeth | Depth | Bore | Other | Ratio |
| 14mm | 8mm | 2012-2016 | SR | 30 | 15mm | 1" | key measurements? | 130 | 15mm | 1" |  | 4.33:1 |
| 〃 | 〃 | 〃 | FX/FXS | 25 | 〃 | 〃 | 〃 | 132 | 〃 | 〃 | 〃 | 5.28:1 |
| 〃 | 〃 | 〃 | S/DS/DSR | 28 | 〃 | 〃 | 〃 | 130 | 〃 | 〃 | 〃 | 4.64:1 |
| 〃 | 〃 | 2017-2018 | S 13.0 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| 17mm | 11mm | 〃 | FX/FXS/DS/DSR/SR/S6.5 | 20 | 17mm |  | spline measurements? | 90 | 17mm |  |  | 4.50:1 |
| 〃 | 〃 | 2019 | S/DS/SR/DSR/FX/FXS | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |

**Reference**

[2013 DS chain drive](http://electricmotorcycleforum.com/boards/index.php?topic=6689.msg53623#msg53623)

[Re: Big belt Kits for pre-2017 bikes.](http://electricmotorcycleforum.com/boards/index.php?topic=6538.msg51446#msg51446)

#### [Sprocket Wear On Belt](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt/Wear_From_Sprocket_Debris)

Wear debris from the tire or the road can accumulate on sprocket teeth, putting pressure on the belt which can wear it out faster.

**Recommendation**

Keep the sprocket teeth clean to minimize wear on the belt.

A non-abrasive brush should be effective.

#### [Front Sprocket Removal / Swap](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Sprocket_Replacement)

Removing or replacing the front sprocket on S and X platforms.

**Video Guide**

Some guidance from Terry in this [motor removal thread](http://electricmotorcycleforum.com/boards/index.php?topic=6230):

- Basically, if you are doing this to try to get more acceleration by moving from a 28 tooth to a 25 tooth, Harlan recommends trading in the DS on a 2015+ SR or 2016 DSR if you need the off road capabilities. You will get much much more acceleration and not hurt your top end performance.
- On the drive belt side, the upper rear 5mm bolt takes **extreme** care to remove. It is tapered to locate the motor. There is a very strong chance of stripping the head and have to drill it out. Make sure to have a machine shop close by just in case.
- On the other hand, removal of the motor may not be necessary.

- The other 7 bolts, 3 on the sprocket side and 4 on the rear brake side are the only thing simple and straight forward.

  You will need a special 3" or longer 6mm allen head socket for sticking in the hole through the frame at the front of the motor.

  1. Remove the rear brake pedal and assembly to get the heel guard out of the way of the top right rear motor bolt.

     Be careful not to strip these bolts either.

     They have Loctite; use a torch.

     And make sure your local hardware store has these replacement bolts handy in case you have to drill them out.

     The rear brake pedal needs to move anyway to get the right swingarm bolt out.
- Also the sprocket bolt itself, as well as removing and installing the new sprocket on the shaft can be very difficult. Some of the best professionals have had trouble.

  Loctite has been used on everything and you will need a torch to remove them.

  Even so, you will need a strap wrench with an old belt as the strap to hold the sprocket and a high power impact wrench.
- Even with all that right, you have a chance of stripping or breaking the bolt. The sprocket is pressed pretty tight.
- Be very careful not to permanently damage the motor bearings by prying between the motor itself and the sprocket to try to remove it, and also by tapping with a hammer to try to fit the new one on. You will be tempted to do both, but you need to find another way.

  A gear puller would be much better.
- There are other things to watch for:
  - Mark your phase leads and pay special attention to the routing.
  - Don't over-tighten the motor jack nuts and bolts until you have the swingarm back in place as it can pull the frame together slightly making it impossible to get the swingarm in place.
  - Make sure you unplug the 8 way motor encoder harness and it doesn't get yanked and pull a wire.
  - The top shock mounting bolt is a 15 and 17 mm and can be done with ratchet wrenches 1/32 of a turn at a time, or without ratchet wrenches if you are known to have extreme patience. It can take a while. The 2014 is a little easier and is (seems to be a) dual 17mm bolt and nut.
  - The swingarm bolts are 10mm allen head and can be extremely hard to relocate even when working with someone else, a rubber hammer, and a flashlight. Those who have replaced their own belt before can vouch for this.
- Again, I doubt too many on this forum have done this, and those who did I'll bet agree with me that it makes more sense after they did it and perhaps had their bike out of commission to work through the things that didn't go right, and would agree to just upgrade to the SR or DSR first vs trying to change the front sprocket.
- Also the 25 tooth sprocket will break belts easier as less teeth are engaged than the 28 tooth, which can make it more likely to sheer teeth in the event of a wheelspin, and it bends the belt at a sharper radius which can possibly fatigue the carbon strands more. The SR actually uses a 30 tooth front sprocket which is even nicer to the belt than the 28 tooth.

## [Brakes](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Brakes)

Zero's [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) models have single-disc brakes for front and rear systems.

### [Brake Maintenance](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Maintenance)

- Check for pad wear or debris.

  Keep the pads and discs clean.

  An occasional brushing of the disc holes is worth doing maybe once a year.
- Check hydraulic fluid level.

  Make sure the brake fluid is in good shape and the type/specs you need.

  If in doubt, replace with fresh fluid (not from an already opened bottle).
- Make sure the brake fluid reservoir is not over-filled (top).

  There has to be some empty space, or your bike will be lightly "braked" and your disk/pads will deteriorate prematurely...and you will get less range.

### [Brake Systems](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Systems)

|  | Front |  |  | Rear |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Year | Manufacturer | Rotor | Caliper | Manufacturer | Rotor | Caliper | Notes |
| 2013 | Nissin | 313mm (listed) / 310mm (actual) ⌀ <br> - floating <br> - matches KTM 450SMR |  | Nissin | 221mm ⌀ <br> - fixed |  | relatively weak <br> [J Juan upgrade](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_6&products_id=211) available for rear brake. |
| 2014 | 〃 | 〃 | 〃 | J Juan | 240mm ⌀ | S: 34mm <br> X: 30mm | Same pad sizes as 2013. |
| 2015 | J Juan | 320mm ⌀ <br> - non-floating <br> M8x23mm shoulder screw fasteners | S: 32/30mm <br> X: 27mm | 〃 | 〃 | 〃 | Bosch Gen 9 ABS; New pad sizes. |
| 2016 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | Bosch Gen 9 ABS |
| 2017 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| 2018 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| 2019 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| 2020 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |

### [Brake Hydraulics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Hydraulics)

| Models |  | Front |  |  |
| --- | --- | --- | --- | --- |
| Platform | Years | Caliper Piston Area | MC Piston Area | Hydraulic-Advantage Ratio |
| S | 2015 | 1509 mm² (total) | 126 mm² | 11.9:1 |
| 〃 | 2016 | 〃 | 〃 | 〃 |
| 〃 | 2017 | 〃 | 〃 | 〃 |
| 〃 | 2018 | 〃 | 〃 | 〃 |
| 〃 | 2019 | 〃 | 〃 | 〃 |
| 〃 | 2020 | 〃 | 〃 | 〃 |

**[Regarding Brake Upgrades:](http://electricmotorcycleforum.com/boards/index.php?topic=6631.msg52829#msg52829)**

A 9.5mm-piston master cylinder - like the Nissin 3/8 I put on my 'MX' bike - would give the SR a 21.1:1 ratio, or @ 78% more pad pressure than the OEM 12.7mm master cylinder.

Any Brembo, Nissin, etc. 9.5mm / .375" master cylinder w/switch should drop right in and make a huge difference, and you won't have to touch anything else.

On the rear, the 11mm master cylinder from the FX (Zero part# 25-06731) has 49mm M6 bolt spacing / rear reservoir hose / top output / clevis, and should give @ 19% more pad pressure than the SR 12mm master cylinder.

This won't be a night-and-day difference like the front master cylinder change, but it should still be very noticeable.

### [Rear Brake Actuator](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Rear_Brake_Actuator)

The rear brake is manipulated by a dirt-bike style pedal around the right [footpeg](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Footpegs), a common motorcycle configuration.

![S and DS foot pedals compared](../images/Footpeg-comparison.gif) *S and DS foot pedals compared*

The rear brake has its own master cylinder behind the rear footpeg on the right.

**Pedal Construction**

Cast aluminum with a powder coat finish.

On pre-2015 models, the pedal is made from a single piece.

On 2015+ models, the pedal toe actuator is bolted on (M6X20-8.8) and may be replaced or have an S vs DS toe actuator swap.

**Rear Brake Switch**

The rear brake switch is activated hydraulically by pressure in the rear brake system.

The rear brake switch is built into top banjo bolt.

**Rear Brake Pedal**

The threaded rod from the brake lever to the master cylinder adjusts lever height.

**Rear Brake Pedal Adjustment**

The rear brake pedal is adjustable at the clevis.

1. Remove the pin.

   The *pin* is the part that connects the brake pedal to the clevis.

   The *clevis* is the fork shaped part that goes either side of the sheet metal pedal.
2. Loosen the actuator shaft locknut above the clevis.
3. Grip the shaft firmly with (say) long heavy-duty needle-nose pliers.
4. Rotate the shaft clockwise (back toward the rear of the bike) to lower the pedal foot.

   Or counterclockwise (towards the front) to raise the pedal foot up.
5. Tighten the locknut back up to hold the clevis in place.
6. Put the pin back in.

**Rear Brake Pedal Spring**

On most models, there is a spring suitable for a dirt bike that is over-designed for a street bike.

There is a kind of spring inside the brake pump, so the external one is just to keep the foot-pedal without rattling.

**Suggestion:** Remove the rear brake spring or replace it with a lighter spring.

Test the rear brake after doing this.

**References**

[Re: [2016 FXS](http://electricmotorcycleforum.com/boards/index.php?topic=6618.msg52588#msg52588) Rear brake light comes on way too late]

[Is there an adjustable pedal brake lever?](https://electricmotorcycleforum.com/boards/index.php?topic=9424)

[Rear Brake Pedal mods](https://electricmotorcycleforum.com/boards/index.php?topic=7266)

[DSR Rear brake lever height adjustment](https://www.electricmotorcycleforum.com/boards/index.php?topic=9888)

### ABS System

2015+ models have a Bosch ABS system installed.

#### ABS Unit

#### ABS Wheel Sensors

### [Brake Pads](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Pads)

Zero Motorcycles models use disc brakes with consumable brake pads applied by calipers to the rotors.

**General Reading Material**

[Top 10 Questions About Motorcycle Brake Pads](http://www.bikebandit.com/blog/post/top-10-questions-about-motorcycle-brake-pads)

[Motorcycle Brake Pads & Rotors Explained, by Galfer USA](http://www.bikebandit.com/blog/post/motorcycle-brake-pads-and-rotors-explained-by-galfer-usa)

[Sintered vs Organic Brake Pads](http://powersports-blog.denniskirk.com/5573/powersports/motorcycle-brake-pads-sintered-vs-organic/)

**General Brake Pad Replacement Suggestions**

- **2013+ ([Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2), [Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3)):** Try to not use synthetics pads or "sintered", but organic or semi sintered ones.

  Sintered are better for very aggressive riding/braking, but are generally noisier.
- **2012 and earlier ([Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1)):** Keep the sintered pads

  Brake pump is very weak on these models; you need all the braking power you can get in spite of noise.

Sand the pads.

Grease the back of the pads lightly with ceramic grease (copper grease can interfere with ABS sensors).

Check caliper position.

Check caliper springs, if any.

Check the wheel for trueness.

Sand the disk; it could have lightly crystalized.

Make sure all the bolts in the system (including wheel) are properly tightened.

After all of this has been preformed and before riding, clean everything exposed to dirt/grease with isopropyl alcohol

When riding again, try to not brake very aggressively the first 20-30 miles.

#### [Brake Problems](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Problems)

This covers general problems with brake pads, in terms of typical symptoms.

**Brake Squeak**

Brake *squeak* (pad front against the disc) happens occasionally and is relatively quiet and noticeable but not anomalous.

**[Brake Squeal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Squeal)**

Brake *squeal* (pad back resonating against caliper cylinder) can be very loud and annoying. Squeal does not technically impact performance but it's very unpleasant and might cause the rider to hesitate before fully braking which is a safety issue.

**Solutions**

- Clean the pads and/or discs for squeaking.
- Try a [different brake pad](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Pad_Lookup) (attractive if you want a different pad feel or performance in the first place).
- LocTite Disc Brake Quiet stick applicator for the backs of the pads.
- [Chamfer the brake pads](https://www.facebook.com/groups/zmcowners/permalink/1329769437092261/?comment_id=1334269306642274&comment_tracking=%7B%22tn%22%3A%22R%22%7D)

  File the edges of the pad to put a 45 degree edge on them

  You only need 1-2mm

#### [Brake Pad Fit](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Pad_Fitment)

**Nissin (2013 on rear, and 2013/2014 front)**

**J Juan (2014+ on rear, 2015+ on front)**

[Front pad shape FDB892](http://ecat.ferodoracing.com/motorcycle/brake-pads-and-shoes/FDB892)

[Rear pad shape FDB539](http://ecat.ferodoracing.com/motorcycle/brake-pads-and-shoes/FDB539)

Past forum threads of highly varying quality / ability to clarify:

- This [forum discussion](http://electricmotorcycleforum.com/boards/index.php?topic=5650) starts with the 14FX and brings up lots of issues.
- Another forum thread on [brake pad alternatives to OEM/stock](http://electricmotorcycleforum.com/boards/index.php?topic=5829).
- One [exhaustive listing from Burton](http://electricmotorcycleforum.com/boards/index.php?topic=3370.msg18646#msg18646) which unfortunately have the wrong EBC fitment numbers.

**EBC**

The [EBC brake catalog](https://ebcbrakes.com/Assets/ecatalogues/EBC_2017_US_MC_Catalog/EBC_2017_US_MC_Catalog.html#p=220) covers Zero models.

However, it has always had the wrong shape recommendation for 2013-2014 models, and for the FX entirely! Double-check any recommendation.

Their Carbon X pads can eliminate front brake squeal. [EBC Carbon X page](https://ebcbrakes.com/product/carbon-x-or-tt-brakes/)

**SBS**

offers a [brake search engine](http://uk.sbs.dk/business-areas/motorcycle.aspx) which covers Zero models.

**Goldfren**

offers a good [cross reference](http://www.goldfrenusa.com/includes/pdf/GOLDFREN_BrakePadsCrossReference.pdf) between brands.

**[Brembo](http://moto.brembo.com/en/)**

Brembo's [Motorcycle Brakes Configurator](http://moto.brembo.com/en/) has reasonably usable Zero model lookup.

Their Carbon Ceramic pads are reported to resolve brake squeal issues.

#### [Front Brake Pad Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Front_Brake_Pad_Replacement)

See [Brake Pad Lookup](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Pad_Lookup) to ensure a brake pad match.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Avoid touching the pad and rotor surfaces with sharp tools and anything dirty or greasy. Avoid applying one-sided pressure to the rotor. |

**2013-2014 S-platform**

Actual bike used was a 2014 SR (Nissin 313mm). Likely applicable to S/DS/DSR.

**Tools**

- 13mm hex socket
- Torque wrench
- 4mm Allen key
- Size 1 flat head screwdriver
- Sandpaper
- Brake cleaner
- Ceramic grease (copper grease can interfer with the ABS sensors)

![Nissin front brake 2014SR loosen bolts](../images/Nissin_front_brake_2014SR_loosen_bolts.jpg) *Nissin front brake 2014SR loosen bolts*

![Nissin front caliper bolts 13mm hex 2014SR](../images/Nissin_front_caliper_bolts_2014SR.jpg) *Nissin front caliper bolts 13mm hex 2014SR*

**Steps**

1. Clean the slave cylinder to prevent forcing damaging detritus into the seal.
2. Gently force the brake pads away from the disk, to ensure room for the new pads, which will be thicker than the worn pads.

   Apply pressure evenly by hand or with a soft-surfaced tool.
3. **Pre-2015:** Using the Size 1 flat blade screwdriver, remove the cap to expose the head of the pin.

   | | |
   | --- | --- |
   | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Penetrating oil may be necessary, and it's important to use the right size flat blade, as smaller ones can strip the slot as you apply pressure. |

   | | |
   | --- | --- |
   | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Rely on the caliper bolts' anchoring to the disc to ensure leverage. |
4. Remove the pin using a 4mm Allen key.

   | | |
   | --- | --- |
   | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Rely on the caliper bolts' anchoring to the disc to ensure leverage. |
5. Remove the 13mm hex bolts holding the caliper to the fork bracket.
6. Remove the caliper from the brake disc; inspect and clean.

   It may be possible to change the brake pads without removing the calipers from the disk, but removal is more thorough to check for wear and keep it clean.
7. Remove the plate with the brake pads, inspect and clean, and put in fresh pads.
8. Apply ceramic grease to the slave cylinders and sand the front surface of the pads.
9. Re-install the pin through the brake pads to anchor them in place.

   Apply a drop of blue Loctite to prevent it coming loose.
10. Re-install the calipers against the rotor:
    1. With the pads separated sufficiently, slide the caliper over the front disc.
    2. Align the caliper mounting holes with the fork bracket and thread the 13mm hex bolts to hold in place.
    3. Apply some blue Loctite to each caliper mounting bolt and tighten with the 13mm hex socket to the right torque ([2014+: 19ft-lb, 2013: 12ft-lb](Fastener_Specifications.md "Fastener Specifications")).
    4. **Pre-2015:** Using the Size 1 flat blade screwdriver and a drop of blue Loctite, re-install and tighten the cap over the head of the pin.
11. Squeeze the front brake lever a few times to build up pressure in the hydraulics and press the pads up to the disc.
12. Test the brakes
    1. Rotate the front wheel to check that the caliper doesn't impede the wheel.
    2. Roll the bike and test the brake lever action.
    3. If there are no obvious problems, gear up and slowly ride the bike to test the brakes.
    4. If possible, gradually increase the speed of the braking tests to seat and smooth the pads.
    5. Perform an initially very slow test ride (walking speed up to 25mph), checking brake function and ensuring they are seated and performing adequately.

**2015+ S Platform**

Actual bike used was a 2016 SR

1. Locate the bolt used to pin the low side of the brake pads.

   Remove the clip on the inside of the bolt.
2. Detach the ABS wire from the brake line, by carefully unclipping the lower three fasteners holding the ABS wire to the brake line.
3. Remove the bolt pinning the pads with a #25 Torx bit.
4. Back out the caliper bolts with a 8mm hex bit on a 12-inch or longer wrench.
5. Remove the caliper from the rotor.
   1. Complelely remove the caliper bolts and slide the caliper as far as possible off the rotor.
   2. With a flat screwdriver about 8-inches long, drop the inside pad out of the caliper.
   3. After the inside pad clears the caliper, remove the caliper.
6. Temporarily hold the old pads against the pistons by loosely replacing the bolt that pins the pads.
7. Fully push back the pistons, by using a C-clamp with at least 2x2-inch opening and 1-inch heads, clamping the old pads to the outside caliper body.
8. Remove the clamp and old pads.
9. Test fit the new pads.
10. Insert the outside pad in the caliper.
11. Hold the caliper against the rotor and insert the inside pad.
12. Re-install the calipers against the rotor:
    1. Position the caliper to insert the caliper bolts, and tighten a little more than finger-tight.
    2. Carefully drive the pad-pinning bolt until it stops, and reinstall the inboard clip.
    3. Remove the caliper bolts one at a time, apply Loctite 242 or equivalent, and retighten.
    4. Torque the caliper bolts to 19 lb-ft (26 Nm).
    5. Re-attach the ABS wire to the brake line (via the 3 clips).
13. Squeeze the front brake lever a few times to build up pressure in the hydraulics and press the pads up to the disc.
14. Test the brakes
    1. Rotate the front wheel to check that the caliper doesn't impede the wheel.
    2. Roll the bike and test the brake lever action.
    3. If there are no obvious problems, gear up and slowly ride the bike to test the brakes.
    4. If possible, gradually increase the speed of the braking tests to seat and smooth the pads.
    5. Perform an initially very slow test ride (walking speed up to 25mph), checking brake function and ensuring they are seated and performing adequately.

#### [Rear Brake Pad Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Brake_Pad_Replacement)

**Tools**

- T25 Torx bit screwdriver

  ![Torx T-25](../images/Torx_t25.jpg) *Torx T-25*
- Flat blade screwdriver
- Small pliers
- 200 grit sand paper (optional)

**Steps**

![J Juan Rear Brake Calipers](../images/Rearbrakes_jjuan.jpg)

1. Remove safety spring-clip from the rear of the bolt (on the side of the wheel).

   Just push it out with a flathead screwdriver.

   ![J Juan pin with its safety clip.jpeg](../images/J_Juan_pin_with_its_safety_clip.jpeg)![Rear Brake E-Clip](../images/Rearbrakeclip.jpg)
2. Remove the bolt that goes through the "eye" of the brake pads (using #25 torx driver).

   ![Rear Brake Bolt](../images/Rearbrakebolt.jpg)![Rear Brake Bolt with tool](../images/Rearbrakeboltwithtool.jpg)
3. Pull out the pads.

   They just come out when pulled gently by hand towards the rear of the bike.

   ![Rear Brake Pads](../images/Rearbrakepads_jjuan1.jpg) ![Rearbrakepad jjuan remove left.jpg](../images/Rearbrakepad_jjuan_remove_left.jpg) ![Rearbrakepad jjuan remove right.jpg](../images/Rearbrakepad_jjuan_remove_right.jpg)
4. If there's any debris like paint on the pad material, you may want to sand them flat/clean gently over some 200 grit sandpaper on a flat surface.
5. Put in new pads.

   ![Jjuan rear 2014 old vs new.jpg](../images/Jjuan_rear_2014_old_vs_new.jpg)
6. Screw-in the bolt.

   ![Jjuan rear 2014 new installed.jpg](../images/Jjuan_rear_2014_new_installed.jpg)

   It maybe good to use some anti-seize paste if not present from the factory.

   Torque value unknown, but be quite gentle - probably something like 10lb/ft (hand-tighten firmly with a regular screwdriver kind of torque).
7. Reinstall safety clip.
8. Test your ride carefully!

**References**

Per [Rear Pad Replacement](http://electricmotorcycleforum.com/boards/index.php?topic=5933.0) for J Juan rear brakes (2014+)

## Powertrain

The powertrain includes all of Zero's power storage and delivery components including the battery, but this section focuses on the [motor](#Motor), power delivery via the [controller](#Controller), and their inputs via [throttle](#Throttle) and drive mode configurations.

**Licensing**

- For a time, Zero openly offered powertrain components in a licensed manner for prototyping and other uses.
- Currently, probably for reasons of liability and support overhead, this is not publicly offered but does seem available on request for companies wanting to develop products where Zero's powertrain is a good fit.
- See Zero's [Z-Force Powertrain Solutions](https://www.zeromotorcycles.com/powertrains/) page which has a contact form.

### [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle)

The Zero throttle is a very straightforward twist-grip motorcycle control that operates a sensor instead of pulling on a mechanical cable or operating hydraulics.

Zero switched the throttle supplier from a [Magura](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Magura_Throttle) with a linear potentiometer to a [Bitron](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Bitron_Throttle) with a Hall-effect sensor in 2015 which changed how the wiring works.

**Connections**

The Zero throttle connects directly to the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller), so anything you do related to the throttle signal can compromise the operation of the bike if there's an electrical fault or discrepancy.

**Example:** [Sudden braking followed by no motor/throttle response on highway[2016 FXS](http://electricmotorcycleforum.com/boards/index.php?topic=6548)]

**Customization**

See [Drive Modes](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Modes) to customize throttle input interpretation as an owner.

Use the mode control for "Custom" mode on 2014+ or "Eco" on earlier models to set the maximum torque the throttle applies.

This also directly changes how quickly torque ramps up for a given throttle twist/position.

**Advanced Customization**

The Sevcon motor [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) settings are where most of the throttle interpretation happens.

**Replacement**

TODO...

**Assembly**

The return spring cannot be tensioned while disassembled throttle is on the handlebar. Throttle must be removed to place the spring end correctly. see video from Harlan Flagg: <https://www.facebook.com/harlanflagg/videos/1364143910276196/>

**Troubleshooting**

[One report of a "snatchy" throttle](http://electricmotorcycleforum.com/boards/index.php?topic=6382.msg49746#msg49746) turned out to have this explanation:

There is a black adjusting screw which holds the pinion gear of the throttle in place or for adjustment.

The pinion gear had moved to the right and caused the spring clip for throttle return to pop out of the slot.

This was clicking through the gears and causing a notchy throttle feel.

Resolution: Reset the pinion location and tighten the screw.

#### [Magura Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Magura_Throttle)

The 2012-2014 stock throttle is a [5kOhm Magura throttle](http://www.evdrives.com/product_p/thr-magura-assy.htm)

**Basic details**

The Magura Twist Throttle has a 0-5kΩ output.

Comes with matching grip for opposite side.

7/8" (22mm) handle bar fit

68" long control cable

Weight: 0.5 lbs

**Connectors**

Three wire output directly to the [controller](#Controller).

| Wire | Function | Destination | Illustration |
| --- | --- | --- | --- |
| Blue | Throttle High | Sevcon Pin 34 | ![Throttle-magura-connector.png](../images/Throttle-magura-connector.png) |
| Brown | Wiper | Sevcon Pin 22 (analog) | 〃 |
| Orange/Black | Throttle Low | B- Sevcon terminal | 〃 |

#### [Bitron Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Bitron_Throttle)

2015+ models use a new HAL-based (Hall-effect active device) sensor from [Bitron](http://www.bitron.net) which can't be replaced easily by Domino or similar

Product reference: [Bitron HAL-based throttle](http://www.bitron.net/index.php?option=com_k2&view=itemlist&task=tag&tag=accelescooter&Itemid=231)

**Connectors**

Via [Keith's investigation](http://electricmotorcycleforum.com/boards/index.php?topic=6966.msg57299#msg57299)

8 wire output, bundled into two pairs of 3 wires for potentiometer outputs.

![Throttle-wiring-bitron.png](../images/Throttle-wiring-bitron.png)

[Sumitomo connector 6188-0779](http://prd.sws.co.jp/components/en/detail.php?number_s=61880779)

[Sumitomo connector 6189-1240](http://prd.sws.co.jp/components/en/detail.php?number_s=61891240)

The hall-effect sensor may be a potentiometer wired up as a voltage divider as follows:

| Wire | Twist | Voltage |
| --- | --- | --- |
| Brown | None | 0.5 |
| 〃 | Full | 4.5 |
| Brown/Red | None | 4.5 |
| 〃 | Full | 0.5 |

### [Regen](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Regen)

Regen refers to [Regenerative Braking](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Regenerative_Braking)

**Operation**

The Sevcon [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Controller) can enter a regeneration mode where it captures momentum from the motor and charges the battery.

The battery must accept incoming power for this feature to work, and the controller must manage the process.

**Operating Range**

Regen for Zeros operates between 12mph (where the motor cannot produce enough voltage to naturally power through the controller) and 4500 RPM (70mph in default gearing).

This band can be adjusted in [MBB settings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console).

**Level**

Regen levels are defined/set in terms of percentage of maximum allowable levels, so 0-100%.

That 100% maps to a 40A recharge limit setting in the Sevcon controller, equivalent to 10% of the maximum discharge rate of a Gen4 size 4 controller.

The 100% setting also corresponds to 60% of the 72Nm torque limit also specified.

The recharge limit may be set up to 91A via Sevcon setting or higher by a dummy value (65535?).

Zero sets regen levels to preclude rear wheel lockup, so raising the limit is a risk that ABS cannot directly control.

Regen has the same effect for SR/DSR models as for S/DS.

**Efficiency**

The recharge efficiency of regen is typically that 10% of the energy used to climb an incline can be returned on the corresponding descent.

**Triggers**

- Normal regen is triggered by relaxing the throttle.

  There is a position just above the resting position where an actual neutral torque is achievable.

  The [MBB has a setting](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) in mV for the potentiometer output of the throttle to trigger regen.

  Adjusting this is not normally effective unless changing throttle types.
- Brake regen is triggered by the same signal that turns on the brake light:

  A contact switch against the front brake lever will engage the brake light (and regen); the hydraulic piston and the switch engage simultaneously by default.

  Rear brakes engage pad contact and the brake light (and regen) simultaneously, but require some amount of travel before they engage.

### [Drive Modes](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Modes)

The Zero platform has always offered a simple control for switching throttle and regen mappings through MBB-Sevcon interaction.

**[Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1) (2009-2013)**

- Through 2013, only Eco and Sport modes were available, where Eco was the customizable mode but had the Eco default as listed below.
- The modes are selected with a rocker switch on the left part of the steering head bracket forward from the handlebars.

**[Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) (2014-)**

- 2014 models introduced a separate Custom mode and made Eco mode fixed.
- Modes are selected by pressing a selector button on the right hand switch assembly; the selected mode then activates when the throttle is released for a couple of seconds.

**[Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3)**

- The [SRF Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SRF_Model) introduced "Street, Sport, Eco, Rain and up to 10 programmable custom modes".
- Custom traction control modes were also introduced.

| Mode | Max Speed | Max Torque | Max [Regen](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Regen) | Max [Regen](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Regen) Brake |
| --- | --- | --- | --- | --- |
| Eco | 70 mph | 40% | 66% | 100% |
| Custom | 70 mph | 100% | 40% | 66% |
| Sport | 98 mph | 100% | 40%? | 66%? |

**[Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) Customization**

Many riders make their own Custom mode settings. There are many options that all involve tradeoffs.

- 0% (-20%) Max Regen

  This enables a "coasting" mode which is very efficient, in allowing the rider to let the bike's momentum carry it forward for a while.

  This also helps transition the bike from accelerating to decelerating, since the regen levels come on in a step-wise fashion, which minimizes the dive on the suspension by providing an intermediate step.

  **NOTE:** This has one disadvantage at 0%: in extremely low traction scenarios, this can lead to dangerous fishtailing where the rear wheel starts to slip, in that it can be very difficult to slow it down.
- 100% Max Brake Regen

  Most riders seem to leave this setting at 100% in order to get the most out of their rear brake.
- Lower Top Speed (60 or 70mph, say)

  This creates a "poor man's" cruise control, where the throttle has no effect at the top end, only ensuring that a specific speed is met.

  This can be useful when trying to get a maximum or ensured amount of range.
- Lower Max Torque (30% or less)

  This can be useful in wet or reduced traction conditions.

  Torque setting is mostly about the torque ramp rate (how much torque achieved with a given amount of throttle twist).

  By reducing the ramp rate, the onset of a loss of traction is much easier to control and recover from.

  Most riders just switch to Eco mode in the rain, but using Custom mode for this can also be effective.

### [Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor)

All of Zero's motors are air-cooled and mounted on a shaft that is aligned with the front pivot of the swingarm so that transmission tension is perfectly aligned with swingarm movement.

| Gen | Brand | Designation | Years | Models |
| --- | --- | --- | --- | --- |
| [Gen1](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1) | [Agni/Saietta](http://www.saiettaengineering.com/motors/) | [95-R](http://www.robotcombat.com/products/EMS-AGNI-B-95R.html) [alt](http://www.asmokarts.com/index.cfm?pageID=24) | 2009-2011 | S/DS/X/MX |
| 〃 | [Motenergy](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motenergy) | [ME0810](http://www.evdrives.com/product_p/mot-me0810.htm) | 2011-2012 | X/MX |
| 〃 | 〃 | [ME0913](http://www.motenergy.com/me0913.html) | 2012 | S/DS |
| [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) | [Z-Force Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) | [75-5](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-5) | 2013 | FX/MX/XU |
| 〃 | 〃 | 〃 | 2014-2015 | FX |
| 〃 | 〃 | 〃 | 2016 | FX/FXS |
| 〃 | 〃 | [75-7](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-7) | 2013-2016 | S/DS/MMX |
| 〃 | 〃 | [75-7R](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-7R) | 2014-2015 | SR |
| 〃 | 〃 | [75-7R](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-7R) ([IPM](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/IPM_Update)) | 2016-present | SR/DSR |
| 〃 | 〃 | [75-5](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-5) ([IPM](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/IPM_Update)) | 2017-present | FX/FXS/S/DS ([Longbrick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Longbrick)) |
| [Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3) | 〃 | [75-10](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-10) ([IPM](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/IPM_Update)) | 2020-present | SRF/SRS |

#### [Agni Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1/Agni_Motor)

![AgniMotor.jpeg](../images/AgniMotor.jpeg)

From 2009 to 2012, Zero used brushed DC [Agni/Saietta](http://www.saiettaengineering.com/motors/) [95-R](http://www.robotcombat.com/products/EMS-AGNI-B-95R.html) motors.

These have known quality issues after time and Zero offers many owners a [Z-Force motor](#Z-Force_Motor) upgrade or complete trade-in for remaining 2014 models.

**Basic Facts**

Shaft ⌀19mm

6mm keyway

~22 kW (30 HP)

**Chain Specs**

420 chain specs: .500" pitch / .3125" roller diameter / .250" roller width / .227" sprocket width.

#41 sprocket teeth will engage 420 chain links, but they're made for .306" dia. rollers and a #41 sprocket / 420 chain combo will wear quickly.

Some sprocket places sell '41/420' sprockets, but there's no such thing.

**References**

[2012 to 2013 motor upgrade info](http://electricmotorcycleforum.com/boards/index.php?topic=5123)

[Jack Shaft sprocket source](http://electricmotorcycleforum.com/boards/index.php?topic=7168.0)

#### [Z-Force Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor)

[![Z-Force™ Motor](../images/Motor-illustrated.png)](http://www.zeromotorcycles.com/technology/)

![Z-force-motor-opened.png](../images/Z-force-motor-opened.png)

For the 2013+ models ([Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) and [Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3)), Zero has [their own motor design](http://www.zeromotorcycles.com/technology/), trademarked "Z-Force".

**Features**

- Sealed
- Air-cooled (via finned casing)
- Brushless
- Permanent-magnet rotor

**Operation**

It is a 3-phase [*brushless DC* (BLDC) electric motor](https://en.wikipedia.org/wiki/Brushless_DC_electric_motor) which is [roughly described](http://electricmotorcycleforum.com/boards/index.php?topic=3640) as a *permanent magnet AC synchronous* (PMAC) motor since the controller is continuously adjusting the phase angle of the field to the rotor's current position and speed.

The field must apply synchronously to the rotor, so the calibration between the position sensor and the [controller](#Controller) is critical for efficiency, minimizing wear on the bearings, and minimizing heating of the windings and magnets.

**Motenergy's Clone**

[Motenergy](http://www.motenergy.com/) makes [an unlicensed generic derivative](http://www.motenergy.com/mepmbrmo.html), the [ME1507](http://ev-power.com.au/webstore/motors/motenergy-me1507.html), of the same form factor, rated for much lower outputs and seems to differ from Zero's motor in key ways.

From [Motenergy's ME1507 product page](http://ev-power.com.au/webstore/motors/motenergy-me1507.html), it's clear that they're advertising a model on par with the 2016 IPM update:

> The ME1507 is an Radial Air Gap, Permanent Magnet Synchronous Motor (PMSM) with an Internal Permanent Magnet Rotor (IPM). Designed for battery pack voltages of 100 VDC or less. Maximum rotor speed of 6000 rpm. Continuous current of 200 amps, and continuous power of 17 kw. Weight of 44 pounds.

**Motor theory**

[IPM vs SPM](http://www.motioncontrolonline.org/content-detail.cfm/Motion-Control-Technical-Features/Interior-Permanent-Magnet-Motors-Power-Traction-Motor-Applications/content_id/789) for a different motor control regime but some principles translate to the Z-Force motor.

**Efficiency**

[forum thread](http://electricmotorcycleforum.com/boards/index.php?topic=4070)

[Range vs Speed by Patrick Truchon](http://ptruchon.pagekite.me/wiki/rangevsspped) discusses the theory and measurements in depth.

[Does Gear Size Affect Range? by Patrick Truchon](http://ptruchon.pagekite.me/wiki/blog/2015-09-19/does_gear_size_affect_range) with more theory!

##### [Z-Force Motor 75-5](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-5)

The [XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform) uses the 75-5 variant of the [Z-Force Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor), as well as the [Longbrick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Longbrick) S/DS models (2017-present).

The **-5** suffix indicates a 5cm extruded width.

##### [Z-Force Motor 75-7](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-7)

The [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) used the 75-7 variant of the [Z-Force Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) from 2013-2017.

Later platform models diverged; SR/DSR models used the 75-7R motor and S/DS models with [Longbrick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Longbrick) batteries and storage compartments adopted the 75-5 variant.

The **-7** suffix indicates a 7cm extruded width.

##### [Z-Force Motor R-Variant](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-7R)

The 75-7R motor follows on the [75-7](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-7) in 2014 with high-temperature magnets.

These require [Sevcon](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Sevcon) Gen4 size 6 controllers to deliver more current and torque

SR (2014+) and DSR (2016+) models use these motors.

##### [Z-Force Motor IPM Update](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/IPM_Update)

In 2016, Zero introduced an interior permanent magnet (IPM) design as distinguished from a surface permanent magnet (SPM) design of the original motor introduced in 2013.

- An IPM design places the rotor magnets in physical slots within its circumference, instead of binding the magnets to the rotor's circumference via special epoxies.
- The IPM design reduces the heating associated with developing magnetic flux and distributes the heat produced more evenly.

  This allows the motor to operate at higher outputs while producing less heat overall and concentrating heat production where it dissipates more easily.

  In practice, this avoids hitting thermal limits which require cutbacks to protect the motor windings.

**Controller Programming Note**

- The IPM design motor apparently involves custom Zero programming of the Sevcon controller for the encoder, so off the shelf DVT software cannot perform alignment/commissioning but can apply settings / DCF files and restore them.

**Production / Rollout**

- 2016 models S/DS/SR/DSR/FXS have the IPM design.
- FX and S/DS models with a 3-brick battery retained the SPM design (presumably to be phased out with inventory).
- As of 2017, statements from Zero indicate that once the IPM motor design was in production, SPM motor production ceased, and all replacements of SPM motors would use IPM motors.

**References**

[Zero livestream announcing 2016 upgrades](http://livestream.com/accounts/14139273/events/4442461)

[Zero livestream presentation with Ryan Biffard about the Z-Force motor IPM upgrade](http://livestream.com/accounts/14139273/events/4534534)

##### [Z-Force Motor Mount/Torque Update](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/Splined_Shaft_Update)

In 2017, the [Sevcon](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Sevcon) [controllers](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) were updated ("4.5" is the unofficial revision) to support more current to the motor.

The [Drive Belt](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt) was also reinforced and widened to apply more torque through the transmission and be more robust against interference.

Accordingly, the motor shaft is now *splined* instead of *keyed* so the motors and sprockets are not compatible across the 2016-2017 year-line.

##### [Z-Force Motor 75-10](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/75-10)

The [FST Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FST_Platform)/[Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3) uses the 75-10 variant, which has a new construction in addition to being wider.

- Cooling ridges run along the circumference of the cylinder rather than axially parallel to the shaft.

  These ridges align with directional airflow from under the frame where the motor controller enclosure guides it.
- The construction therefore is no longer an extrusion as in previous casings.

  Possibly there are lathe-like methods involved in machining.
- The finish in the first model with the motor is bronze, probably indicating something about an alloy change.
- **-10** suffix indicates 10cm length.

**Features**

- The motor encoder position sensor is now housed in a servicing-accessible enclosure, opposite the shaft, on the right side.
- The motor mounts are now more structural, joining the swingarm to the rear of the main frame.

  TODO review for a better structural description.

**Notes**

- There was a comment about lamination improvements inside the motor for better heat transfer which will probably get a cutaway illustration soon.
- The team were also proud of designing the new motor; it seems to be fabricated in a relatively distinct way, perhaps even unique.

  They regretted that their existing extrusion method went by the wayside, because they relished being able to "just lengthen the motor" to get different performance levels out of it, and the new motor design does not afford that in the manufacturing implementation.

#### [Motor Mounting](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Mounting)

On the [motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) there are 8 M8 bolts holding the motor in place: 4 on the drive side, 4 on the rear side.

Those bolts only have about 12Nm of torque on them.

**References**

[Burton's 2013 to 2014 motor swap thread](http://electricmotorcycleforum.com/boards/index.php?topic=5218) shows the most detail about the physical mounting of the motor.

#### [Motor Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Removal)

**Tools**

- M8 Allen socket
- Torque wrench

**Steps**

1. [Perform a lockout on the powertrain](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lockout_Procedure).
2. [Remove the swingarm](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Swingarm_Removal).

   First you have to remove the swing-arm (that is pretty straight forward) some big bolts in the pivot and disconnet the shock.

   You can leave the brake lines attached and just move the swingarm out of the way when the motor needs to come out.
3. Unplug the sensor connector near the front of the contoller on the riders right side of the bike.
4. Un-bolt the 3 phase leads to the motor controller.

   It's a good idea to insulate them just in case the bike is powered on.
5. Disconnect the motor from the bike.

   On the motor there are 8 M8 bolts holding the motor in place: 4 on the drive side, 4 on the rear side.

   Those bolts only have about 12Nm of torque on them.
6. Once you have the motor disconnected and un-bolted from the frame, it should slide out towards the back.

#### [Motor Bearing Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor_Bearing_Replacement)

This replaces the [motor bearings on Gen2 Z-Force motors](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/Bearings).

**Tools**

- C-clip pliers
- M10 tensioner
- Loctite 648
- Hub puller (to extract the bearings)
- Replacement bearings (front and rear are both 6006-2RS on an FX used below)

**Notes**

- In these instructions, the *front* of the motor is the left/shaft-side, and the *rear* of the motor is the right/encoder-side.

**Steps**

1. Prepare a clean workspace, removing all debris and metal tools that you are not directly using.

   | | |
   | --- | --- |
   | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | The rotor magnets are so strong they rip tools out of your hand and they attract every single metal filing that might be near by. |
2. [Remove the motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor_Removal) from the bike.
3. Removed the belt pulley:
   1. Remove the M10 countersunk bolt.
   2. Put two thin pieces of metal under the pulley, and drive two M6x1? bolts into the two threaded holes of the pulley to lift the pulley off.
4. Gently pry the front cover off.

   It will most likely be stuck on the rotor so you'll be lifting the rotor out of the housing with it.

   It is actually quite straighforward to pull apart, but requires a lot of force.

   You can built a little chair (width of the plate, you put it on the cooling wings) with an M10 tensioner.

   Then you bolt an M10 eye-bolt (or T-handle) on the pulley so you can pull on the shaft really hard (about 200lbs), and the rotor will pull out on the shaft along with the drive plate and bearings.

   | | |
   | --- | --- |
   | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Once you have the shaft and rotor out, be careful as it is highly magnetic and you can get your fingers pinched quite easily on it. |

   At that point, the rotor should be loose on the shaft.
5. If you have to remove the rear bearing, remove the c-clip holding the rotor laminations on the shaft, use a marker or something to mark the front and back of the rotor and how it is aligned on the shaft because you are going to take it off.

   The end of the rotor on the back side is aluminum so do **not** press on it.

   It houses tiny magnets that the motor position sensor (encoder) reads; damage to this will ruin the rotor.

   | | |
   | --- | --- |
   | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | It is important that it goes on in the exact same direction, otherwise the motor could spin backwards. |
6. Once you have the rotor and the shaft labeled so you can get them back together exactly the same way, slide the rotor laminations off the shaft.
7. Clean the shaft and the inside of the laminations.
8. Apply a lot of loctite 648 on the shaft and lamniations, then slide them back together.

   Ensure that they go together the same way that they were before.

   Endure that the loctite 648 gets well-distributed between the shaft and the laminations to make a solid bond.
9. Press the rotor out of the front cap

   The bearing is held into the cap by a retainer so the rotor is pressed from the bearing.
10. Remove the front bearing retainer and press the bearing out of the cap.
11. Put the c-clip back on, put the bearing back on (or put a new bearing on since removing a bearing without damaging it is quite hard, the front and rear bearings are both 6006-2RS).

    | | |
    | --- | --- |
    | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | When you put the new bearing on, make sure you just push on the inner race for the press fit, if you push on the outer race it will transfer the force through the balls and likely damage them. |

    The bearing should be a press fit; if it slips on or off easily, you should glue it on with the loctite 648.
12. Let the 648 cure for a few hours before putting the motor back together.
13. To put the motor back together, just do the same thing you did to pull it apart, but opposite.

    Ensure that the wave-spring is still in the bottom of the bearing pocket at the bottom of the motor.

    | | |
    | --- | --- |
    | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Be careful to not let the rotor slam back into place, that could damage the bearing |

    Temporarily lining the inside of the stator with a plastic sheet can prevent damage to the stator and rotor.

    Make sure you control the rotor: use the little chair and unscrew the tensioner to let the magnetic forces pull it back in slowly.

    Once it is almost all the way in, the bearing will catch on the bearing pocket.

    At that point, it might take a little jiggling around and some force on the end of the shaft to get it to pop into place, then it could take a bit more force to get the drive-plate to re-engage with the stator case.

#### [Motor Shaft](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/Shaft)

**Pre-2017**

The motor shaft is keyed; the key has a square cross section.

**Measurements**

- Dimensions seem to be ¼” square ⨉ 2.0” length (expressed in metric on drawings).
- Ends 5mm from shaft end.
- Shaft diameter is ⌀28.275mm+0-0.021
- Shaft length extends 66.675mm beyond the motor face minus 4mm for raised parts of the face.

2013 models had a minor [recall](Recalls.md "Recalls") about the shaft key coming loose, but this was a design revision that has not recurred.

**2017+**

The motor shaft is splined to allow higher torque transmission.

Rumor has it (via [Harlan at Hollywood Electrics](http://electricmotorcycleforum.com/boards/index.php?topic=7010.msg59925#msg59925)) that the spline is supposed to match a Kawasaki KX250F as well as a Yamaha YZ450F.

#### [Motor Sounds](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/Sounds)

The [Z-Force Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) family has many characteristic sounds worth minding and distinguishing.

Because the motor is so quiet overall, anomolous sounds should be more notable, from say bearings, sprockets, or the belt.

##### [Motor Whirring](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor_Whirring)

The [motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) on 2013+ models makes a white noise sound at very slow speeds when rotated (by the wheels or shaft).

This is also described as a "whirring sound".

This is alluded to by the term "[cogging](https://en.wikipedia.org/wiki/Cogging_torque)".

This is normal as long as it sounds like white noise and occurs as described below.

**Video Guide**

- [Strange noise Zero DS 2017](https://www.youtube.com/watch?v=UtKvr9d35VU) provides a reference for comparison:

**Related Confirming Symptoms**

- The noise should *only* occur while the motor is rotated by external input (pushing the bike around or rotating the shaft).
- The noise should *not* while under power (when the motor is driving its own rotation).
- The bike should gently resist being pushed while the noise is audible.

**Causes**

- The direct cause is the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) applying a white noise field to the motor at very slow speeds.
- At least one connected battery's [contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) *must* have been engaged for this to occur.

  This can occur while keyed on, or while charging.

**Effects**

- There are no detrimental effects, when the sound occurs by design.
- The purpose is for the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) to detect and maintain precise knowledge of the motor's rotor angle.
- This ensures that, if the throttle demands operation, the controller will apply the field correctly to the rotor.
- You may infer that *at least one contactor is engaged* to power the controller.
- If the bike is keyed on, you may infer that the motorcycle should be ready to drive.

  (aside from the [kickstand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Switch) and [kill switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kill_Switch) safety interlocks).

##### [Motor Whine](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor_Whine)

While moving, the [motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) tends to make a solid smooth tone resonant with the motor's rotational speed.

**Related Confirming Symptoms**

- Typically, this occurs while the motorcycle is traveling at speeds above 10mph.
- Most noticeable between 15-30mph (30-50kph).

**Causes**

- The motor shaft bearings are likely the primary generator of this resonant noise.

**Effects**

- None; this is normal and expected.

#### [Motor Wiring](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/Electrical_Connections)

The Z-Force motor's stator is connected to the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) for power and position feedback.

| | |
| --- | --- |
| 3-phase / Y-shaped (120° phase offset) power inputs from the controller. <br> 1. A (M1) <br> 2. B (M2) <br> 3. C (M3) | ![Motor-controller power connections](../images/Motor-controller.png) *Motor-controller power connections* |

| | |
| --- | --- |
| 8-pin Metri-Pack 150 ([Mouser p/n 829-12047937](http://www.mouser.com/ProductDetail/Delphi-Connection-Systems/12047937/)) <br> - Terminal: [Mouser p/n 829-12084200](http://www.mouser.com/ProductDetail/Delphi-Connection-Systems/12084200/) <br> - Retainer: [Mouser p/n 829-15324525](http://www.mouser.com/ProductDetail/Delphi-Connection-Systems/15324525/) <br> - Seal: [Mouser p/n 829-15324973](http://www.mouser.com/ProductDetail/Delphi-Connection-Systems/15324973/) <br> - Seal: [Mouser p/n 829-12059168-B](http://www.mouser.com/ProductDetail/Delphi-Connection-Systems/12059168-B/) <br> 1. Motor Position (Cosine) / white <br> 2. Motor Position (Sine) / blue <br> 3. Motor Position (Ground) / black <br> 4. *unused* <br> 5. [VDD](https://en.wikipedia.org/wiki/IC_power-supply_pin) (5V) / red <br> 6. Shield / green <br> 7. Temperature (negative) / yellow <br> 8. Temperature (positive) / yellow | ![2013 motor sensor connectors](../images/Motor-signals-connector.png) *2013 motor sensor connectors* |

#### [Motor Alignment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Alignment)

Motor alignment refers to physical alignment of the motor with the frame and swingarm so that power is transmitted correctly to the final drive.

The back side of the motor (encoder side) has screw jack bolts that let you tweak the motor position.

Mostly this is only needed when (re)installing the motor.

**Steps**

1. Loosen the four M6 socket head screws.
2. Adjust the portion of the silver nut that is not wedged into the slot on the motor.

#### [Motor Commissioning](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor_Commissioning)

Motor commissioning refers to aligning the controller's sine wave programming against the motor using its position sensors.

**Benefits**

Maximum efficiency (avoids current applied wastefully)

Avoid any slippage.

Avoid misapplied torque which might wear on the bearings.

#### [Motor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/Limits)

The following regards what engineering constraints limit the power and RPM of the (IPM) Z-Force motor. Pre-IPM motors generated more heat for a given amount of power, so cooling was usually the first concern, but the IPM design pushes the frontier further so the topic is worth addressing.

**RPM**

The Z-Force motor is design-limited to 6,000 RPM as follows.

RPM is primarily limited by the inductance of the motor windings.

At low RPM, under full throttle, the current through the driven phase(s) of the motor ramps up from 0 to the maximum allowed by the controller pretty quickly, and you get full torque because you've got full current.

But the faster the motor turns, the faster the motor controller has to cycle the phases of the motor on and off, and eventually, you reach a point where there's not enough time (because of the inductance of the motor windings) for the current to ramp up to maximum before that phase has to be turned off and the next phase cycled on.

At that point, power starts to drop off, so very shortly after that, the motor won't have enough torque or power left to drive the load.

The mechanics of the motor could easily have been designed for higher RPM, but there's no point since you'll be current-limited anyhow.

**Torque / Power**

The easiest way to get more torque, and thereby more power (since power is proportional to torque times RPM), is to pump more current through the motor.

Several things can bottleneck that effort:

- First, the motor windings have a DC resistance because they're copper wires with fixed gauges and lengths.
- The bike's wiring external to the motor also has some DC resistance in it.
- If you apply more voltage to a fixed DC resistance, you'll get more current, but the batteries only give you ~110VDC to play with....and of course, the battery has a current limit of its own.
- You'll need to be sure the controller can handle the current as well; you won't go very fast once you smoke the controller.
- Since the motor rotates and therefore the windings have to be commutated (driven on and off in the proper sequence and speed), the motor's inductance also comes into play as discussed above about RPM.
- You could change some of this stuff fairly easily (higher-gauge wiring is pretty simple, though might be tough to fit in some of the tight confines the Zero's wiring is routed through), but other things are more difficult.
- To reduce the motor winding's DC resistance, you'd want to use heavier wire, but you wouldn't be able to get as many turns onto the same coil form.
- Fewer turns would create less inductance, which also helps allow higher current levels, but fewer turns also results in a weaker magnetic field for the same current, so you might actually reduce the torque the motor puts out.
- Then you'd also need to be sure you don't over-current the controller, or the batteries, and cooling everything involved becomes an additional topic.

It's kind of like asking what's the highest VO2 max an athlete can put out.

- It's not just about his lungs, it's about his heart, his muscles, his metabolism at a microscopic level, even about his mental attitude.
- Tweak any one thing and the system's whole balance shifts.
- That's why engineers make the medium-sized bucks!

**Speed**

Vehicle top speed can only be altered by the gearing (sprocket ratios).

Power output is not affected by gearing; only torque is.

So, a ratio yielding a higher top speed will result in lower torques throughout the range, resulting in slower accelerations from start.

**References**

[What is the limit of a Zero motor?](http://electricmotorcycleforum.com/boards/index.php?topic=7208.0)

### [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller)

The motor controller takes power from DC battery bus, encoding three-phase sine waves to match the motor's position sensor to apply torque precisely to the motor.

![Sevcon Gen4 Size 6 Controller Top](../images/Sevcon_Gen4_Size_6_Controller_Top.png) *Sevcon Gen4 Size 6 Controller Top*

[Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) motor controllers are all Sevcon Gen4 motor controllers, mostly Size 4 (S/DS) and Size 6 (SR/DSR), with Size 2 for the older XU model.

The sine waves are constructed by power transistors operating in a [pulse-width modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation) (PWM) capacity.

The power is applied to the motor in synchronization with the current speed and position of the rotor.

Controller alignment ([motor commissioning](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor_Commissioning)) is the process of tuning all of this for maximum efficiency and to avoid any slippage.

#### [Controller Operation](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Operation)

The controller is a switching [MOSFET](https://en.wikipedia.org/wiki/MOSFET) power supply that creates 3 phased sine wave outputs to drive the motor via [Pulse-width modulation](https://en.wikipedia.org/wiki/Pulse-width_modulation) (PWM).

The switching attempts to produce a smooth sine wave to each output terminal via [Space vector modulation](https://en.wikipedia.org/wiki/Space_vector_modulation) strategy of PWM.

The motor has 3 stator (casing-embedded) windings at 120° equally spaced offsets around the circumference.

- Each winding pulls from one motor terminal's output from the controller.
- Each winding electromagnetically pulls on the rotor.
- The forces need to balance out, not leading to a net lateral force on the rotor and shaft.
- It also shouldn’t precess or wobble or slip.

The process of making the sine waves is “encoding”.

![MY2017 Zero SR.  Scope at Sevcon M3 Output Terminal](../images/My2017sr-sevcon-scope.jpg) *MY2017 Zero SR. Scope at Sevcon M3 Output Terminal*

#### [Controller Alignment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Alignment)

*Alignment* is the calibration of the controller sine wave production to match the controller output to the motor's position precisely.

- This is performed once/first by Zero's [Motor Commissioning](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor_Commissioning) process and then repeated later as a recalibration.
- It should generally be performed periodically as a preventative maintenance step.

The motor has sensors for encoder alignment to tell the exact angle of rotation of the rotor.

- If those sensors are inaccurate, encoding can be rough or fail entirely.
- The sensors are embedded within the motor so for owners they just compensate in the controller for the drift, or swap the motor if the signal is bad enough that the controller can’t work with it.

#### [Controller Versions](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Versions)

| Bike |  | Controller |  | Limits |  |
| --- | --- | --- | --- | --- | --- |
| Years | Models | Manufacturer | Model | Input Voltage | Phase Current |
| 2009-2011 | S/DS | [Alltrax](http://www.alltraxinc.com/) | [AXE4855](http://www.alltraxinc.com/Products_AXE.html) refs: [[8]](http://www.evdrives.com/product_p/con-axe4855.htm) [[9]](http://www.electricmotorsport.com/alltrax-axe4855-24-48v-500a.html) | 48V | 500A |
| 2012 | XU | [Sevcon](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Sevcon) | [Gen4](http://www.sevcon.com/products/low-voltage-controllers/gen4/) [Size 2](http://ev-power.com.au/webstore/sevcon/gen-4-size-2-80v.html) | 120V | 220A |
| 〃 | S/DS | 〃 | [Gen4](http://www.sevcon.com/products/low-voltage-controllers/gen4/) [Size 4](http://ev-power.com.au/webstore/sevcon/gen-4-size-4-80v.html) | 〃 | 420A |
| 〃 | X/MX | [Alltrax](http://www.alltraxinc.com/) | [AXE7245](http://www.alltraxinc.com/Products_AXE.html) refs: [[10]](http://www.evdrives.com/product_p/con-axe7245.htm) [[11]](http://www.electricmotorsport.com/alltrax-axe7245-24-72v-450a.html) | 72V | 450A |
| 2013-2016 | XU | [Sevcon](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Sevcon) | [Gen4](http://www.sevcon.com/products/low-voltage-controllers/gen4/) [Size 2](http://ev-power.com.au/webstore/sevcon/gen-4-size-2-80v.html) | 120V | 220A |
| 〃 | S/DS/FX/FXS/MMX | 〃 | [Gen4](http://www.sevcon.com/products/low-voltage-controllers/gen4/) [Size 4](http://ev-power.com.au/webstore/sevcon/gen-4-size-4-80v.html) | 〃 | 420A |
| 〃 | SR/DSR | 〃 | [Gen4](http://www.sevcon.com/products/low-voltage-controllers/gen4/) [Size 6](http://ev-power.com.au/webstore/sevcon/gen-4-size-6-80v.html) | 〃 | 660A |
| 2017+ | S/DS/FX/FXS/MMX | 〃 | [Gen4](http://www.sevcon.com/products/low-voltage-controllers/gen4/).5 [Size 4](http://ev-power.com.au/webstore/sevcon/gen-4-size-4-80v.html) | 〃 | 550A |
| 〃 | SR/DSR | 〃 | [Gen4](http://www.sevcon.com/products/low-voltage-controllers/gen4/).5 [Size 6](http://ev-power.com.au/webstore/sevcon/gen-4-size-6-80v.html) | 〃 | 775A |

**2017 “Gen4.5”**

2017 models reference higher current ratings without publicized evidence of a Sevcon model change.

These improvements seem to be in choosing [MOSFETs](http://www.mouser.com/new/Infineon-Technologies/infineon-optimos-5/) with increased power switching efficiencies to allow higher continuous and peak current levels.

“Gen4.5” has been a term heard describing these improvements.

**Gen4 Size 6 Controller**

- ![](../images/Sevcon_Gen4_Size_6_Controller_Top.png)

  Sevcon Gen4 Size 6 Controller Top
- ![](../images/Sevcon_Gen4_Size_6_Controller_Top_Connections.png)

  Sevcon Gen4 Size 6 Controller Top Terminals
- ![](../images/Sevcon_Gen4_Size_6_Controller_Connectors_Left_Side.png)

  Sevcon Gen4 Size 6 Controller Terminals Left Side
- ![](../images/Sevcon_Gen4_Size_6_Controller_Connector.png)

  Sevcon Gen4 Size 6 Controller Connector
- ![](../images/Sevcon_Gen4_Size_6_Controller_Left_Side.png)

  Sevcon Gen4 Size 6 Controller Left Side
- ![](../images/Sevcon_Gen4_Size_6_Controller_Front.png)

  Sevcon Gen4 Size 6 Controller Front
- ![](../images/Sevcon_Gen4_Size_6_Controller_Rear.png)

  Sevcon Gen4 Size 6 Controller Rear
- ![](../images/Sevcon_Gen4_Size_6_Controller_Bottom.png)

  Sevcon Gen4 Size 6 Controller Bottom

**Gen4 Size 6 Controller Internals**

- ![](../images/Sevcon_Gen4_Size_6_Controller_Connection_Front_(Uncovered).png)

  Sevcon Gen4 Size 6 Controller Connection Front
- ![](../images/Sevcon_Gen4_Size_6_Controller_Connections_Profile_(Uncovered).png)

  Sevcon Gen4 Size 6 Controller Connections Profile
- ![](../images/Sevcon_Gen4_Size_6_Controller_Connectors_Left_Side_(Uncovered).png)

  Sevcon Gen4 Size 6 Controller Connectors Left Side
- ![](../images/Sevcon_Gen4_Size_6_Controller_Cover_(Underside).png)

  Sevcon Gen4 Size 6 Controller Casing
- ![](../images/Sevcon_Gen4_Size_6_Controller_Top_(Uncovered).png)

  Sevcon Gen4 Size 6 Controller Top

#### Controller Mounting

##### [SDS Controller Mounting](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Controller_Mounting)

**Controller Location**

The [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) is located beneath the seat at the front of the tail assembly.

**Controller Fasteners**

The baseplate is fastened from the underside of the tail of the frame, between the frame "horns".

A [plastic sheet cover](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Cover) is fastened across the top of the controller by a Phillips head screw (PH1).

A [heatsink](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Heatsink) is fastened to its surface for radiative cooling, with a thermal paste between to maximize heat transfer via contact/conduction.

4 M6 bolts secure the controller baseplate to the frame.

- For size 2 and size 4 controllers, the base plate is 12mm thick.
- For size 6 controllers, the base plate is 20mm thick.

##### [XMX Controller Mounting](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Controller_Mounting)

**Controller Location**

The controller is positioned in the lowest part of the forward face of the frame, just in front of the motor.

**Controller Fasteners**

A [heatsink](#Controller_Heatsink) is fastened to its surface for radiative cooling, with a thermal paste between to maximize heat transfer via contact/conduction.

4 M6 bolts secure the controller baseplate to the frame.

- For size 2 and size 4 controllers, the base plate is 12mm thick.

#### [Controller Uncovering](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Controller_Uncovering)

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | This exposes high-voltage terminals that can damage tools, equipment, or cause injury or death if not de-energized. <br> Ensure the bike is fully de-energized or that you are using professional methods and safety precautions. |

**Prerequisites**

- [Remove the seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Seat_Removal)

**Tools**

- Small Philips-head screwdriver (PH1)

**Steps**

1. Use the Philips head screwdriver to unfasten the rear end of the sheet just aft of the controller in the tail.
2. Pull up carefully to raise the edges out from under the tail frame's side rails.
3. (Optional) Wind the forward section of the plastic sheet counterclockwise around the AMPSeal 34-pin connector, pulling on the left.

#### [Controller Heatsink](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Heatsink)

The underside face of the controller is directly covered by a finned heatsink that faces downwards toward the rear wheel and swingarm.

- The heatsink varies in size with the size of the controller.
- A thermal paste is applied between the heatsink and baseplate to maximize heat transfer via contact/conduction.
- The rear shock connects just ahead of the heatsink to the frame center tube.

#### [Controller Connections](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Connections)

| | |
| --- | --- |
| Main terminals are, in order from front to rear: M1, B-, M2, B+, M3. <br> For Size 4 and Size 6, the bolts are all M8 with a torque setting of 11Nm±2Nm; bolts should engage a minimum of 10mm and thread depth is 15mm. <br> For Size 2 (2013XU), the bolts are all M6 with a torque settings of 7Nm±2Nm. <br> - M-terminals supply the motor with its rotating field in three phases. Each gets a sine wave that is offset by 0, 120, 240 degrees. <br> - B+ and B- connect to the battery power at positive and negative, respectively. | ![Motor-controller power connections](../images/Motor-controller.png) *Motor-controller power connections* |
| [Connector info](http://www.te.com/usa-en/product-1-776163-1.html) (see AMPSEAL Automotive Plug Connector and Header Assembly (PDF, English)) <br> [More connector info](http://www.mouser.com/Search/ProductDetail.aspx?qs=YqNA2qefETAUziSpjzx9mg%3d%3d) (look at bottom for pins) | ![2013 Gen4 Size 4 Controller signal connector](../images/Controller-connector.png) *2013 Gen4 Size 4 Controller signal connector* |

**Diagnostic Cables**

![Sevcon programming cable harness](../images/Cable-harness-sevcon-prog-all.png)![Connections to Sevcon for programming](../images/Cable-harness-sevcon-prog-ampseal-34-rear.png)![34-pin AMPSeal connector](../images/Cable-harness-sevcon-prog-ampseal-34.png)

Zero Sevcon programming cables are part #86-06747 connected as follows:

- Pin 1 is "Key Switch In": power for the logic circuits.
- Pin 2 is linked to pin 24 via 120Ω resistor to tell the Sevcon that it's at the CANBus termination.
- Pin 13 is "CAN High".
- Pin 27 is "CAN Low" in the Sevcon manual (pin 24 also is, unless used for termination signal).

#### [Controller Feature Usage](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Feature_Usage)

This describes how the [Sevcon controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller)'s features are used on Zero models.

**Throttle**

[Sevcon](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Sevcon) provides the [throttle](#Throttle) with two mappings:

1. Mapping voltage to value in the first place (separately for forward and reverse)
2. An "input characteristic" profile which has linear, curved, crawl, and user-defined segmented options.

The controller also supports:

- Control modes targeting speed (used through 2012) versus torque (used in 2013+).

  The control mode translates the throttle signal into motor operation, so it makes the throttle target a speed or a level of torque.
- Dual throttle inputs.
- Regen proportional to the throttle.
- Directional throttle.
- Speed limit proportional to throttle.
- Reverse speed limit.

**Regen**

The [Sevcon](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Sevcon) controller manual refers to regen as braking, and has a number of recommendations and features disabled to help prevent wheel lockup for "on-highway applications".

**Braking**

The Sevcon can also apply reverse torque as braking or a reverse gear, and supports separate speed and torque limits while the motor is rotating in reverse, very important if used on a Zero since motorcycles are unstable when reversed so must operate within human walking speeds.

**OEM Programming**

Zero programs the Sevcon controller for their needs, above and beyond DOT, NHTSA, and EU vehicle manufacturing standards.

Some of this is a bunch of settings and some of this seems to be a custom version of the firmware code.

The new IPM motor may have demanded further customization than previous models, where custom firmware code is particularly relevant.

*Settings* can be changed and restored, but not *code* without some OEM-supported technical assistance.

#### [Controller CAN Diagnostics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/CAN_Diagnostics)

Via the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) logs or the [console](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console), emergency (EMCY) entries related to `SEVCON` will be CAN controller events from the [Sevcon Gen4 drives](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller).

**Example logged events**

via [Re: Sudden braking followed by no motor/throttle response on highway(2016 FXS)](http://electricmotorcycleforum.com/boards/index.php?topic=6548.msg57769#msg57769)

```
07004     06/03/2017 09:30:18   SEVCON CAN EMCY Frame      Error Code: 0x5000, Error Reg: 0x40 Sevcon Error Code: 0x46c3, Data: 0x04 0x01 0x00 , Unknown
07005     06/03/2017 09:30:18   SEVCON CAN EMCY Frame      Error Code: 0x   0, Error Reg: 0x00 Sevcon Error Code: 0x46c3, Data: 0x00 0x00 0x99 , Unknown
07006     06/03/2017 09:30:18   SEVCON CAN EMCY Frame      Error Code: 0x5000, Error Reg: 0x40 Sevcon Error Code: 0x46c3, Data: 0x04 0x02 0x00 , Unknown
07007     06/03/2017 09:30:18   SEVCON CAN EMCY Frame      Error Code: 0x   0, Error Reg: 0x00 Sevcon Error Code: 0x46c3, Data: 0x00 0x00 0x99 , Unknown
07008     06/03/2017 09:30:18   SEVCON CAN EMCY Frame      Error Code: 0x5000, Error Reg: 0x40 Sevcon Error Code: 0x52c3, Data: 0x00 0x00 0x00 , Unknown
07009     06/03/2017 09:30:18   SEVCON CAN EMCY Frame      Error Code: 0x5000, Error Reg: 0x40 Sevcon Error Code: 0x46c3, Data: 0x0c 0x10 0x00 , Unknown
07010     06/03/2017 09:30:18   Restarting Sevcon to clear cutout fault
07011     06/03/2017 09:30:18   Module 00                  vmod: 112.127V, batt curr: 65498A
07012     06/03/2017 09:30:18   Module 01                  vmod: 112.156V, batt curr: 65506A
07013     06/03/2017 09:30:19   Sevcon Turned Off
```

**CAN message examples**

```
ID    b0 b1 b2 b3 b4 b5 b6 b7
"81";"00 31 04 C3 4D 00 00 00"
"81";"00 31 14 C3 4D 00 00 00"
"81";"00 82 10 0F 53 02 00 00"
"82";"00 10 01 54 4F 00 40 00"
"82";"00 10 11 54 4F 00 40 00"
"82";"00 31 04 C2 51 00 00 00"
"82";"00 31 04 C2 51 00 04 00"
"82";"00 31 04 C3 4D 00 00 00"
"82";"00 31 05 C3 4D 00 00 00"
"82";"00 31 15 C3 4D 00 00 00"
"82";"30 81 10 0B 53 01 00 00"
```

**Bytes b1+b0 (switch bytes)**

Bytes b1+b0 (switch bytes) describes [CANopen](https://en.wikipedia.org/wiki/CANopen) error code according to [DS-301](https://www.can-cia.org/standardization/specifications/)

| Error code (hex) | Error description |
| --- | --- |
| 00xx | Error Reset / No Error |
| 10xx | Generic Error |
| 2xxx | Current |
| 3xxx | Voltage |
| 4xxx | Temperature |
| 50xx | Device Hardware |
| 6xxx | Device Software |
| 70xx | Additional Modules |
| 8xxx | Monitoring |
| 90xx | External Error |
| F0xx | Additional Functions |
| FFxx | Device Specific |

**Byte b2**

Byte b2 is error register, bit-wise coding, also according to DS-301

| Bit | Error cause |
| --- | --- |
| 0 | Generic Error |
| 1 | Current |
| 2 | Voltage |
| 3 | Temperature |
| 4 | Communication Error |
| 5 | Device Profile Specific |
| 6 | Reserved (always 0) |
| 7 | Manufacturer Specific |

**Bytes b5-b7**

If any of bytes b5-b7 are not 0x00 means error is set.

If bytes b5-b7 are all 00 it means the error is reset.

Might be only b6?

**Bytes b4+b3 (switched bytes)**

Bytes b4+b3 (switched bytes) describes Sevcon specific errors

| Code | Interpretation | Notes |
| --- | --- | --- |
| 0x2401 | Login |  |
| 0x3441 | Host SW Upgrade |  |
| 0x3442 | DSP SW Upgrade |  |
| 0x34C1 | Watchdog Reset |  |
| 0x45C1 | BDI Warning | Battery Discharge Indicator's remaining charge is less than warning or cutout levels. Charge the battery. |
| 0x45C2 | BDI Cutout | 〃 |
| 0x45C3 | Low battery |  |
| 0x45C4 | High battery |  |
| 0x45C5 | High capacitor |  |
| 0x45C6 | Vbat below rated min | Charge the battery! Or the B+ or B- terminals have been disconnected or damaged. |
| 0x45C7 | Vbat above rated max | The battery voltage is detected above 117V or 118V; discharge it through another safe load. |
| 0x45C8 | Vcap above rated max |  |
| 0x45C8 | Vcap above rated max |  |
| 0x45C9 | Motor low voltage |  |
| 0x45CA | Motor high voltage |  |
| 0x4601 | Device too cold | The controller (or motor?) needs to warm up before operating. |
| 0x4602 | Device too hot | The controller (or motor?) is too hot; reduce power to cool it down; check cooling fin bracket. |
| 0x4603 | Motor in thermal c/b | The motor's defined temperature limit has been exceeded so power cutbacks are engaging. |
| 0x4681 | Preop |  |
| 0x46C3 | Ride-Through Fault | [Low-voltage ride through?](https://en.wikipedia.org/wiki/Low_voltage_ride_through) |
| 0x4781 | Anon EMCY |  |
| 0x47C1 | Service Required |  |
| 0x4881 | Seat |  |
| 0x4882 | Two Dir Fault |  |
| 0x4883 | SRO Fault |  |
| 0x4884 | Sequence Fault |  |
| 0x4885 | FS1 Recycle Fault |  |
| 0x4941 | Low oil |  |
| 0x4981 | Throttle Fault |  |
| 0x4B81 | Anon EMCY |  |
| 0x4C41 | Too Many Slaves |  |
| 0x4DC3 | Supply Critical |  |
| 0x4F01 | Bad State |  |
| 0x4F02 | EMCY Fail |  |
| 0x4F41 | Internal Fault |  |
| 0x4F42 | Out of Memory |  |
| 0x4F43 | General DSP Error |  |
| 0x4F44 | Timer Error |  |
| 0x4F45 | Queue Error |  |
| 0x4F46 | Sched Error |  |
| 0x4F47 | DSP Heartbeat |  |
| 0x4F48 | IO SS Error |  |
| 0x4F49 | GIO SS Error |  |
| 0x4F4A | LCM SS Error |  |
| 0x4F4B | LCP SS Error |  |
| 0x4F4C | OBD SS Error |  |
| 0x4F4D | VEHAPP SS Error |  |
| 0x4F4E | DMC SS Error |  |
| 0x4F4F | TracApp SS Error |  |
| 0x4F50 | New PF Detected |  |
| 0x4F51 | DSP not detected |  |
| 0x4F52 | DSP Comms Error |  |
| 0x4F53 | App Mgr SS Error |  |
| 0x4F55 | DSP param |  |
| 0x4F81 | Anon EMCY |  |
| 0x5041 | Bad NVM Data |  |
| 0x5042 | VPDO out of range |  |
| 0x5043 | Param fixed range error |  |
| 0x5044 | Param dyn range error |  |
| 0x5081 | Invalid Steer Switches |  |
| 0x5101 | Line Contactor o/c |  |
| 0x5141 | Line Contactor welded |  |
| 0x5181 | Dig In Wire Off |  |
| 0x5182 | Alg In Wire Off |  |
| 0x5183 | Alg Out Over I |  |
| 0x5184 | Alg Out On with No FS |  |
| 0x5185 | Alg Out Off with FS |  |
| 0x51C1 | Power Supply Interrupt |  |
| 0x51C2 | Precharge fail |  |
| 0x52C1 | Encoder fault | Check the encoder [wiring to the motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor/Electrical_Connections) |
| 0x52C3 | Current Control Fault | Can't control the currents on the [motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor). Check the motor load and wiring; check controller programming. |
| 0x5301 | CANbus Fault |  |
| 0x5302 | No Bootup |  |
| 0x5303 | LPRX CAN |  |
| 0x5304 | LPTX CAN |  |
| 0x5305 | HPRX CAN |  |
| 0x5306 | HPTX CAN |  |
| 0x5307 | CAN Overrun |  |
| 0x5308 | CAN Off |  |
| 0x5309 | Nodeguard Error |  |
| 0x530A | PDO Short |  |
| 0x530B | HBeat Error |  |
| 0x530C | CANopen Device State |  |
| 0x530D | CAN Error State |  |
| 0x530E | SDO Handle Error |  |
| 0x530F | SDO Timeout |  |
| 0x5310 | SDO Abort |  |
| 0x5311 | SDO State Error |  |
| 0x5312 | SDO Toggle Error |  |
| 0x5313 | SDO Rx Error |  |
| 0x5314 | SDO Length Error |  |
| 0x5315 | SDO Tx Error |  |
| 0x5316 | CANopen Ev Unknown |  |
| 0x5317 | SDO Bad Source |  |
| 0x5318 | SDO Bad Error No |  |
| 0x5319 | Mtr Slv in Wrong State |  |
| 0x5341 | Wrong DSP protocol |  |
| 0x5342 | Osc WDog Tripped |  |
| 0x5343 | Flt o/flow |  |
| 0x5381 | Anon EMCY |  |
| 0x54C1 | DSP Overvoltage |  |
| 0x54C2 | DSP PF Fault |  |
| 0x54C3 | Mosfet s/c M1 Top |  |
| 0x54C4 | Mosfet s/c M1 Bottom |  |
| 0x54C5 | Mosfet s/c M2 Top |  |
| 0x54C6 | Mosfet s/c M2 Bottom |  |
| 0x54C7 | Mosfet s/c M3 Top |  |
| 0x54C8 | Mosfet s/c M3 Bottom |  |
| 0x54C9 | Mosfet tests incomplete |  |
| 0x5741 | Invalid Rating |  |
| 0x5781 | Anon EMCY |  |

**Example**

```
ID    b0 b1 b2 b3 b4 b5 b6 b7
"82";"00 31 04 C2 51 00 04 00"
```

Node id 2 sends emergency error.

**Error code:** 0x3100 (b1+b0) meaning "Voltage" error category

**Error cause:** 0x04 (b2) bit 2 set meaning "Voltage" error cause

**Sevcon error:** 0x51C2 meaning "Precharge fail"

#### [Controller Configuration](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Configuration)

The controller's configuration implements a number of Zero features:

- Speed calculations.
- Distance calculations.
- Over-voltage limits to protect the battery by cutting out regen or refusing to operate.
- Under-voltage limits to protect the battery charge state.
- Current limits to protect the battery.
- Delay before regen toggles on or off.
- Driving modes like Eco/Custom/Sport which include speed and torque limits and speed ramping limits to prevent wheel lockup.

**References**

[Sevcon Gen4 product page](http://www.sevcon.com/products/low-voltage-controllers/gen4/) (formerly at [[12]](http://www.sevcon.com/ac-controllers/gen4%E2%84%A2.aspx))

[Gen4 data sheet](http://www.sevcon.com/media/78433/gen4_size_2_4_6_may_2016.pdf) (no longer available without request form with contact details)

[Gen4 reference Manual](http://www.thunderstruck-ev.com/Manuals/Gen4_Product_Manual_V3.0.pdf)

**Configuration**

Some MBB settings direct the Sevcon controller; look to the MBB first.

The MBB can also provide a dump of Sevcon diagnostics and logs.

DVT software to maintain the Sevcon programming is available but recent versions require a license and the cabling is not cheap. The older unlicensed versions may have trouble maintaining newer programming by Zero.

**[Direct diagnostics](http://electricmotorcycleforum.com/boards/index.php?topic=4297)**

For those interested in better understanding your Zero's motor controller setup, you'll need some specific cables and software.

These will allow you to browse the current controller configuration as well as make changes such as increasing regeneration rates, customising sport or eco modes etc.

This is what you'll need:

1. An IXXAT CAN-USB compact adaptor v1.5 (v1.01.0087.10100) or v1.6

   approx USD300 but you may find it cheaper on eBay or borrow/rent it from another forum member or dealer.

   You cannot buy these anymore, you must get them off ebay or part of a [Thunderstruck EV $900 kit](http://www.thunderstruck-ev.com/sevcon-gen4-pc-based-programming-kit.html).

   You cannot use a new version of the IXXAT CAN-USB either as it will not work with an unlicensed copy of the software. And to get a license you have to own a business.
2. A DB2 female to OBDII male cable with a specific pin mapping (not the most common one).

   [Easysync](http://www.easysync-ltd.com/) make a [DB9 female to OBD male cable](http://www.easysync-ltd.com/product/577/obd-m-db9-f-es.html) that has the correct pin configuration - about USD25
3. Sevcon DVT Customer software

   It has to be version 1.03c or lower to use unlicensed (Google is your friend, as is Dropbox in this case).

   Good luck saving your DCF files with it.

   You need to write down your settings before making big changes.

   Even if you bought the new version and got a license you would have to use a NEW IXXAT USB-CAN as the old one isn't compatible.

   The Sevcon software will run on Windows XP, 7 and 8.

   There are manuals and getting started guides on the Internet (Google again) on how to use the DVT software including one at [Thunderstruck EV](https://www.thunderstruck-ev.com/images/DVT%20Tutorial.pdf).

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Do not link any files as they have been removed multiple times in the past. |

- One of the dropbox links you will find will have at least 3 different versions.
- If you install any new versions completely remove everything from the previous versions.
- If you find the program wont start up and it isn't 1.02 then install a "merge" installation of TCL and it should work.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | You can brick your controller temporarily by making changes. |

It would be nice to have a backup but these online versions of "free" sevcon software all have issues with saving.

I have tested 1.00 1.01 1.02 (which never ran) and 1.03c so far.

If you brick your device you will need someone to give you a DCF file to return your device to working order.

But good luck getting it from a form member who doesn't work for a dealer as stated it is next to impossible to export the file.

Sevcon is very much against this use of their product and software, and have issued takedown notices for publicly available files.

You will not get official support and people will be reluctant to post details publicly.

Get the 200 page DVT / SEVCON GEN 4 manual from the manufacture's webpage and read it a couple times.

Try contacting knowledgeable people privately.

You really need to understand what you are doing when you start to make changes.

This isn't a toy you are going to be remotely piloting, it is a vehicle you are risking your life on!

Zero has specific programming to customize the Sevcon controller.

So it is not clear whether customer customization is achievable beyond basic modification of settings or performing an alignment using DVT.

**Recovery**

[DoctorBass has documented a backdoor method of recovering a Sevcon controller if its firmware is in an unusable state](https://endless-sphere.com/forums/viewtopic.php?f=30&t=88205&p=1287062#p1287062)

Using the IXXAT connection, issue the following command:

```
can send "0x7FA 0x48 0x65 0x79 0x73 0x6c 0x69 0x70"
```

This byte sequence is also apparently available as "BD" (for "backdoor", presumably).

#### [Controller Cover](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/Cover)

The motor controller has a sheet installed over it for EMI protection to the rider that is probably also helpful at keeping dust and moisture off.

**[SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) Mounting**

The cover is anchored in front of the controller in a recessed area under the arms of the [Y-Shaped Underseat Subframe](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Subframe).

The cover is anchored to the rear of the controller with a single screw.

##### [Controller Cover Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Controller_Uncovering)

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | This exposes high-voltage terminals that can damage tools, equipment, or cause injury or death if not de-energized. <br> Ensure the bike is fully de-energized or that you are using professional methods and safety precautions. |

**Prerequisites**

- [Remove the seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Seat_Removal)

**Tools**

- Small Philips-head screwdriver (PH1)

**Steps**

1. Use the Philips head screwdriver to unfasten the rear end of the sheet just aft of the controller in the tail.
2. Pull up carefully to raise the edges out from under the tail frame's side rails.
3. (Optional) Wind the forward section of the plastic sheet counterclockwise around the AMPSeal 34-pin connector, pulling on the left.

##### [Controller Cover Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Controller_Cover_Replacement)

**Prerequisites**

1. [Remove the seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Seat_Removal)
2. Remove the [Y-Shaped Underseat Subframe](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Subframe).

**Tools**

- Small Philips-head screwdriver (PH1)

**Steps**

1. Lay the front of the sheet down around the connector wiring and cabling.
2. Insert each side edge carefully under each side rail of the frame's tail section.
3. Push the aft end of the sheet down towards the frame cross-piece behind the Sevcon controller.
4. Fasten the sheet at the aft end with the screw using a small Philips Head (PH1) screwdriver.

## Electronic Systems

### Instrument Cluster

Until 2014, Zero used branded versions of generic Koso instrument clusters, mapping the fuel level indicator to battery state of charge.

#### [Koso XR-SR](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1/Koso_XR-SR)

The Koso XR-SR is a generic/whitelabel instrument gauge cluster, used on 2008-2011 model years.

**References**

- [Koso XR-SR product page](http://kosonorthamerica.com/shop/motorcycle-mx/xr-sr-multi-functions/)
- [instructions](http://www.kosonorthamerica.com/instructions/BB017B00.pdf)

#### [Koso RX-1N](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Koso_RX-1N)

The Koso RX-1N is a generic/whitelabel instrument gauge cluster.

For years 2011-2013, Zero's models have a rebadged version as stock.

![Koso RX-1N (retail)](../images/Koso-rx-1n.png) *Koso RX-1N (retail)*

![Zero's Koso RX-1N cluster (front)](../images/2013-instrument-cluster-Koso-RX-1N-front.png) *Zero's Koso RX-1N cluster (front)*

![Zero's Koso RX-1N cluster (rear)](../images/2013-instrument-cluster-Koso-RX-1N-rear.png) *Zero's Koso RX-1N cluster (rear)*

**References**

- [Koso RX-1N](http://kosonorthamerica.com/shop/motorcycle-mx/rx-1n/)
- [Instructions](http://www.kosonorthamerica.com/instructions/BA011B02.pdf)

**Features**

Zero's RX-1N shows battery level in 11 increments.

It's relatively effective to treat each increment as representing 9% of charge state, and do a little mental math to figure out that each increment could represent 6-12 miles (for say 2013), and work out the remaining range / speed tradeoff from that.

- go slower to get closer to 12 miles of range per increment
- go faster if you can afford to burn off the battery to reach your destination in time.

The Koso instructions linked below show how to operate it.

**Speedometer Adjustment Quick How-To**

- [Reference](http://electricmotorcycleforum.com/boards/index.php?topic=7755)

1. Turn on motorcycle.
2. Press and hold the Select + Adjust buttons simultaneously for 3 seconds.
3. Use the "adjust" button to increment the digit, and the "select" button to navigate to the next digit.

- The stock setting (for 2013) is *1972 28-132 2P*.
- The previous setting (for 2012?) was *1972 25-128 2P*.

**Connections**

Koso connectors are much simpler than Zero's connectors to its own custom dash.

Interchanging them would be a significant project.

![2013 S/DS Koso Display connections](../images/Koso-display-connector.png)

#### [Zero 2014 Instrument Cluster](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster)

In 2014, Zero introduced their own LCD instrument cluster AKA "dash" for all models (S and X platforms).

![Zero 2014 instrument cluster](../images/Dash-2014-drawing.png) *Zero 2014 instrument cluster*

![2014 Zero instrument cluster](../images/Dash-2014.png) *2014 Zero instrument cluster*

**Changes**

The new gauge changed the pin connector and relies on specific CANbus messaging, so there's no simple way to install one on an older model.

It offers an ergonomic advantage that the instrument cluster no longer obstructs access to the keyed ignition and steering lock.

The state of charge reading is now primarily numeric as a two-digit percentage, with a (effectively) continuous bar level reading next to it.

- Disadvantage: no countable number of increments and also making the rider more aware of state of charge calculation nuances.
- Advantage: It's more accurate, and the dash's other functionality (like range and efficiency readouts) easily compensates for remaining inaccuracies.

Zero's [Official Owners Manual](Official_Owners_Manual.md "Official Owners Manual") explains its capabilities pretty well.

**[Indications](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster/Indications)**

| Area | Indicator | Source | Adjustment |
| --- | --- | --- | --- |
| Left | Clock | Internal <br> Powered by a non-replaceable battery | [SEL+ADJ](#Controls) |
| 〃 | Time to Charge | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) | Projected remaining time estimate in hours and minutes. |
| 〃 | [SoC](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SoC) | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) | [MBB settings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) <br> Fuel Gauge Pessimism <br> **NOTE:** The indicator skips 81,61,41,21, and 1. |
| 〃 | Bluetooth Indicator | 〃 | After key-on or the first minutes of charging <br> Unless/until a mobile device pairs <br> See [Unable to Connect](Official_Mobile_Application.md#Unable_to_Connect "Official Mobile Application") and [Pairing](Official_Mobile_Application.md#Pairing "Official Mobile Application") |
| Center | Speed | 〃 | [MBB settings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) <br> Sprocket Teeth Front <br> Sprocket Teeth Rear <br> Rear Wheel Circum |
| 〃 | Odometer | Stored in the unit's memory | Unalterable <br> *If stuck/frozen*, the likely cause is that the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) has misconfigured model information. <br> - Have a dealer examine and correct it, which should propagate an updated reading to this indicator. |
| 〃 | A | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) | To toggle: <br> 1. Press SEL once so that this blinks. <br> 2. Press ADJ to cycle through: <br> - **Trip 1** odometer (resets after a full charge or manually). Units are mi or km. <br> - **Range** estimate, based on a projection tuned by recent ride history. Units are mi or km. <br> - **Error** cycling through the [Error Codes](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Error_Codes) <br> - **RPM** motor rotational speed. Units are RPMs. |
| 〃 | B | 〃 | To toggle: <br> 1. Press SEL twice so that this blinks. <br> 2. Press ADJ to cycle through: <br> - **Trip 2** odometer (resets only manually). Units are mi or km. <br> - **Trip AV** average efficiency over **Trip 1** as Energy/Distance = Power/Speed. Units are Wh/mi or Wh/km. <br> - **Temp** *motor* temperature only. Units are °F or °C. <br> - **Trip AV** average efficiency over vehicle lifetime as Energy/Distance = Power/Speed. Units are Wh/mi or Wh/km. |
| Right | [Drive Mode](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Modes) | 〃 | mode selector switch on right handlebar |
| 〃 | Power | 〃 | [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) |
| 〃 | Torque | 〃 | 〃 |
| Bottom | Left [Turn Signal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Turn_Signals) Indicator | 〃 | Left handlebar turn signal switch |
| 〃 | [System Warning Indicator](https://web.archive.org/web/2025/https://zeromanual.com/wiki/System_Warning_Sequences) | 〃 | Check [System Warning Sequences](https://web.archive.org/web/2025/https://zeromanual.com/wiki/System_Warning_Sequences) |
| 〃 | Temperature Warning Indicator | 〃 | Controller, Motor, or Battery Temperatures at Stage 1 |
| 〃 | Check Engine Indicator (2018+) | 〃 | [Error Codes](Error_Codes.md "Error Codes") triggered permanent torque reduction |
| 〃 | Drive Mode Enabled | 〃 | Green light is: <br> - **Solid** when [contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) shut and cutout disengaged <br> - **Blinking** when [precharging](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/Precharge) <br> - **Disabled/off** by cutout or interlock |
| 〃 | [ABS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/ABS) Indicator | 〃 | Whether [anti-lock braking](https://web.archive.org/web/2025/https://zeromanual.com/wiki/ABS) is operational: <br> - **On** just after startup before reaching 3mph when the ABS tone rings align fully <br> - **Off** while riding unless ABS is engaged. <br> - **On** while riding if ABS is engaged because of a difference between wheel rotational speeds. |
| 〃 | [Charging](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) Indicator | 〃 | Green LED is: <br> - **Flashing** when charging <br> - **Solid** when full <br> - **Off** when riding |
| 〃 | High Beam Indicator | 〃 | Left handlebar [headlamp](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Headlamp) switch |
| 〃 | Right [Turn Signal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Turn_Signals) Indicator | 〃 | Left handlebar turn signal switch |

**Mounting**

This instrument cluster has two M6 (6mm diameter) threaded rods extending from the rear of the enclosure, captured against the plastic shoulder pieces to the headlamp assembly by two 10mm nylon locknuts.

Remove the display before removing the plastic shoulder pieces, and re-intall the plastic shoulder pieces before re-installing the instrument cluster.

**Common Problems**

- Clock skew

  The internal clock is separate from the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board) clock so can drift over time, often faster by minutes per month or so.
- Loss of indication

  When these have issues, it has mostly been due to moisture entering the (relatively well-sealed) housing.

  This can be disassembled for cleaning but would need re-potting with dielectric grease perhaps when re-assembling and need to be very clean and try inside.
- Loss of Clock

  When the clock reads **00:00** and will not respond to adjustments, it is likely that its internal battery has failed.

  Confirm by observing the indications on startup. If "EEE" appears in the main speedometer readout, the battery is likely dead.
- Moisture Ingress

  The instrument cluster's operation depends entirely on being perfectly sealed.

  Any gaps in its insulation can compromise it eventually.

**Diagnostics**

See [MBB Console Dash command](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console)

**Assembly**

**Enclosure**

![Instrument cluster enclosure front with fasteners](../images/2015-instrument-cluster-enclosure-front-with-fasteners.jpg) *Instrument cluster enclosure front with fasteners*

This instrument cluster is enclosed by a plastic housing, with the back half fastened into the front.

The enclosure is fastened by 6 black-finished Philips-head (PH1) machine screws at the rear.

The halves are joined with a rubbery gasket along the edge in a little baffle zone to impede ingress by moisture and dust.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | The seal here appears to be critical to the longevity of the instrument cluster's display and circuits. |

**Internals**

![Instrument cluster board uncovered](../images/2015-instrument-cluster-board-uncovered.jpg) *Instrument cluster board uncovered*

Within the enclosure, the board is fastened to the rear plastic half by 4 Philips-head (PH1) machine screws.

The board's front consists almost entirely of the LCD substrate with no protection - the protective acrylic screen is part of the front half of the plastic enclosure.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Avoid touching the screen or letting dust fall on it. Clean gently with a lint-free cloth as necessary. |

The LCD is connected to the circuitry on the rear of the board by pins along the top edge.

![Instrument cluster board LCD drive pins](../images/2015-instrument-cluster-board-top.jpg) *Instrument cluster board LCD drive pins*

The Select and Adjust buttons trigger micro-buttons on the left side of the board, which have very small plastic extensions linking them to the rubbery buttons.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Take care when uncovering these buttons not to lose the thin button extensions. |

The rear of the board displays the circuitry driving the display.

On the right side of the rear of the board, the internal battery is held.

The battery is a 3V lithium CR2032 cell, which can be replaced with a carefully-chosen cell.

**Connections**

![Instrument cluster board connectors](../images/2015-instrument-cluster-board-connectors.jpg) *Instrument cluster board connectors*

Two connectors at the rear of the board join the circuitry to the signaling interface with the rest of the bike (via CANBus).

The connectors are fastened with a simple clip.

The cable entering the rear of the enclosure is fastened to it by a simple plastic clip and a Philips-head (PH1) machine screw.

Removing the cable should first involve unclipping the board connectors before loosening the screw holding the cable clip.

- ![2015-instrument-cluster-board-back-chip.jpg](../images/2015-instrument-cluster-board-back-chip.jpg)
- ![2015-instrument-cluster-board-buttons.jpg](../images/2015-instrument-cluster-board-buttons.jpg)
- ![2015-instrument-cluster-board-connectors-2.jpg](../images/2015-instrument-cluster-board-connectors-2.jpg)
- ![2015-instrument-cluster-board-connectors.jpg](../images/2015-instrument-cluster-board-connectors.jpg)
- ![2015-instrument-cluster-board-front.jpg](../images/2015-instrument-cluster-board-front.jpg)
- ![2015-instrument-cluster-board-machine-screws-2.jpg](../images/2015-instrument-cluster-board-machine-screws-2.jpg)
- ![2015-instrument-cluster-board-machine-screws.jpg](../images/2015-instrument-cluster-board-machine-screws.jpg)
- ![2015-instrument-cluster-board-rear-left.jpg](../images/2015-instrument-cluster-board-rear-left.jpg)
- ![2015-instrument-cluster-board-rear-right.jpg](../images/2015-instrument-cluster-board-rear-right.jpg)
- ![2015-instrument-cluster-board-rear.jpg](../images/2015-instrument-cluster-board-rear.jpg)
- ![2015-instrument-cluster-board-top-edge.jpg](../images/2015-instrument-cluster-board-top-edge.jpg)
- ![2015-instrument-cluster-board-top.jpg](../images/2015-instrument-cluster-board-top.jpg)
- ![2015-instrument-cluster-board-uncovered-2.jpg](../images/2015-instrument-cluster-board-uncovered-2.jpg)
- ![2015-instrument-cluster-board-uncovered.jpg](../images/2015-instrument-cluster-board-uncovered.jpg)
- ![2015-instrument-cluster-button-plunger.jpg](../images/2015-instrument-cluster-button-plunger.jpg)
- ![2015-instrument-cluster-button-plungers.jpg](../images/2015-instrument-cluster-button-plungers.jpg)
- ![2015-instrument-cluster-enclosure-fasteners.jpg](../images/2015-instrument-cluster-enclosure-fasteners.jpg)
- ![2015-instrument-cluster-enclosure-front-with-fasteners.jpg](../images/2015-instrument-cluster-enclosure-front-with-fasteners.jpg)
- ![2015-instrument-cluster-enclosure-front.jpg](../images/2015-instrument-cluster-enclosure-front.jpg)
- ![2015-instrument-cluster-enclosure-rear-uncovered.jpg](../images/2015-instrument-cluster-enclosure-rear-uncovered.jpg)

### [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger)

How do I move a thread to a different topic?
hi all :)

#### [Calex Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Calex_Charger)

The Calex / [GreenWattPower EVC-116-1300](https://greenwattpower.com/product/1300-watt-evc-li-ion-charger-series/) and [EVC-116-720](https://greenwattpower.com/product/720-evc-li-ion-charger-series/) are used as onboard chargers for modern Zero models (2014 onwards except for the 2014FX) and are CANBus-controllable which eliminates the CCU board.

![Calex connections uncovered](../images/Onboard-charger-rear-uncovered.jpg) *Calex connections uncovered*

![Calex connections](../images/Onboard-charger-rear.jpg) *Calex connections*

**Design**

The board is a solid-state switching power supply with a CAN interface.

The aluminum enclosure is well-sealed with over two dozen fasteners.

The enclosure is filled with a solid rubbery [potting](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Potting) material.

**Reliability**

Certain model years (MY14 and MY15) have had onboard charger faults after 900-1200 miles and require replacement under warrantee.

MY16 onward (and MY13 which used Meanwell units) appear to have a lower defect rate.

This appears to be a third-party quality issue with Calex that was reportedly resolved by early 2016, but this is not proven perfectly yet.

720W chargers used on X models appear to be more reliable than 1300W chargers used on S models.

**Design Revision**

In response to the 2014-2015 reliability difficulties, it seems that the internal board was mainly reworked for lower risk of overheating.

One observation is that the size of the board changed from about ⅓ of the volume of the enclosure to the full area of the enclosure.

Newer revisions seem to have a cube-shaped clip-on ferrite bead EMI filter on the AC input cable (per [this EMF thread](http://electricmotorcycleforum.com/boards/index.php?topic=9049.msg77958#msg77958)).

**Repair**

Because of the solid rubbery potting, repair of anything beyond the connectors is almost totally impractical, especially given the cost of replacement.

The board is designed for blind [replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Calex_Charger_Replacement).

##### [Calex Charger Behavior](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Calex_Charger/Behavior)

Per [CANBUS diagnostic reply](http://electricmotorcycleforum.com/boards/index.php?topic=6330.msg48829#msg48829), the Calex charger operates as a CC/CV mode charger.

- Constant current (CC) mode is the default operational mode.

  The charger attempts to deliver a target amount of current to the battery.

  This means that the charger's power input is proportional to the battery's voltage at that moment, which rises from low state to the high state of charge, so charging will be slower at low voltages (< 20% SoC).
- Maximum allowed battery voltage: 116.4V *(Confirmed via charger self-report over CANBUS)*

  When battery voltage reaches or exceeds this value, the charger enters a constant voltage (CV) mode.

  Since the rate of charge dynamically adds voltage to the pack, the taper eases off this addition so there's a stable charge equilibrium at the end.

  Tapering behavior is observed to reduce output current in increments of 1A and typically starts at 12A.
- Current taper cutoff: 10A *(Confirmed via charger self-report over CANBUS)*

  The charger will cut to 0 output rather than taper below this value.
- Maximum allowed current: 65.535 A *(Confirmed via charger self-report over CANBUS)*

  This is a meaningless binary value.

**Overcharge Protection**

The charger is limited by the manufacturer to a range that matches Zero's battery safe range.

The charger is connected to external AC sources and is therefore a vulnerable component while plugged in.

Per [Re: Change to Charging - Leaving Bike Plugged In](http://electricmotorcycleforum.com/boards/index.php?topic=6707.msg54407#msg54407)

- The charger is an isolated power supply with suppressors on the input.
- So, if a surge were big enough, the suppressors could fail short.
- Then the circuit breaker should fail after that.
- The BMS and the rest of the bike is completely isolated from the charger, so there's no current path to them.

This is why some people on this forum report their charger is dead, but the bike is fine, and there wasn't any fire. Most of the time Zero, replaces the onboard charger for them.

**Worst-case scenario**

- BMS unresponsive
- MBB unresponsive
- Contactor welded
- Charger outputs more than 117.6V

In the event of all these holding (extremely unlikely), there is some risk of a fire.

This is probably why Zero asks you to check on the bike every 72 hours to make sure the bike is still responding and the BMS is still alive.

#### [Meanwell Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Meanwell_Charger)

The [Meanwell](https://www.meanwell-web.com/en/) [HLG-320H-54A](https://www.meanwell-web.com/en/product-info/ac-dc-power-supply/led-driver/gt-185-w-led-driver/hlg-320h/product/HLG-320H-54A) power supplies are used as onboard chargers for early [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) Zero models (2013 and the 2014FX) and are directed by the [CCU](https://web.archive.org/web/2025/https://zeromanual.com/wiki/CCU) board since they lack a CANBus integration.

**Configuration**

- For [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) models, 4 chargers are wired 2s2p for 1.3kW total.

  If any power supply unit fails, the charger should drop to half its output capacity (whether by blowing a fuse or faulting open internally).
- For [XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform) models, 2 chargers are wired in serise (2s1p) for 650W total.

  If either power supply unit fails, the charger will fail to produce output entirely.

**Repair**

- See [Half of a charger fail.](https://www.electricmotorcycleforum.com/boards/index.php?topic=10288)
- It is possible to replace only the dead charger if you have one.

  You'll need big crimping tools and shrinking sleeves.

  Zero sends the full pack of four chargers.

##### [Meanwell Charger Behavior](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Meanwell_Charger/Behavior)

These chargers do not interact over CANBus messaging, so just operate in a preset way in CC-CV mode, although the [CCU](#Charging_Control_Unit) also has some control over it to implement battery protections.

**Clicking Sound**

There is a known issue, per [Clicking sound when plugged-in](http://electricmotorcycleforum.com/boards/index.php?topic=4176), that the Meanwells sometimes make a repeated clicking sound.

It seems to happen generally in the cold.

This symptom does not seem to precede an equipment failure, and should go away once charging is complete.

#### [Charger Operation](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Calex_Charger/Operation)

Mainly, the charger is the most routine bike maintenance and you just plug it in and can forget about it.

**When to Charge**

Per Zero's recommendation, the battery state of charge is ideally kept between 30% and 70%.

- Always plug in when the SoC is below 30%.
- Leave it plugged in to reach 100% and improve cel balance if you are planning to ride the bike in the next few days.
- You can unplug the bike when it reaches 70% if the bike will not be ridden sooner than a few days, or if your next ride will not require more charge.

  This keeps the battery in a healthier state and improves battery lifetime beyond the warranty.

**What to Watch For**

When plugging in, expect:

- The contactor to close with a click or remain closed.
- The dash charging indicator to begin blinking green.
- After a few seconds, (2014+ models) the charge time indicator should display a number of hours and minutes until fully charged.

  This indicator helps predict when a desired SoC can be anticipated, with a little math.

**Trouble Indications**

- Spark at the plug when connecting.
- Heat from the plug.
- No charging dash indicator.
- Circuit breaker trips.

**Reliability Tips**

There is a growing consensus that the Calex charger's limited cooling capacity can lead to damage over time if it's operated repeatedly at the high end of its rated band.

To minimize risk of a charger fault or component burnout, avoid operating it while the battery is hot and still cooling, and address any heating or sparking at the plug.

Check the [Common Charging Problems](Common_Problems.md#Charging "Common Problems") section regarding the plug and cord.

Basic suggestions:

- After an intense ride in the heat with the battery temperature high, wait for a couple of hours until the temperature is lower.
- Keep the inlet covered when not in use.
- Use contact cleaner on the inlet periodically (once per month) or whenever the charging cord plug warms up significantly during charging.
- Minimize strain and load on the charging cord.
- Unplug the cord and cover the inlet when not in use.

**[GFCI](Common_Problems.md#GFCI_Faults "Common Problems")**

Ground fault circuit isolation (GFCI or GFI) enabled outlets often trip when using the Zero onboard charger, relating to how AC phases are wired to a single or multiple outlets.

If this happens regularly, it is reasonable to break off the grounding pin from your charging cord, or, better yet, get a [cheater (three prong to two prong) "cheater" plug](https://www.google.com/?ion=1&espv=2#q=three+prong+to+two+prong+adapter&tbm=shop).

#### [Charger Power Cord](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charger_Power_Cord)

The charging cord is a 10-ft 14AWG cord with a [NEMA 5-15P](https://en.wikipedia.org/wiki/NEMA_connector#NEMA_5) (US) to [IEC320 C13](https://en.wikipedia.org/wiki/IEC_60320#C13.2FC14_coupler) output plug rated for 15A.

Zero specifies that any extension cord be at least the above specification, and 15A continuous rating is important to look for.

**Demand**

- The S-Platform onboard charger draws 11-12A at 120V AC (and half the amps at ~220V).
- The X-Platform onboard charger draws 7A at 120V AC (and half the amps at ~220V).

**Tips**

- When in doubt, prefer a thicker gauge cord, a shorter length, and a sturdier plug.
- Do not let a charge cord sit coiled up, particularly in a container; make sure that any heat produced is not confined near the cord for any reason.
- Plugging into a 220V outlet will reduce the current to the onboard charger by half, so is one way to drastically minimize risk to any cords.

**Replacements**

See [Spare Onboard Charger Power Cables](Common_Modifications.md#Spare_Onboard_Charger_Power_Cables "Common Modifications")

#### [Charger Connections](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Calex_Charger/Connections)

**Calex Charger Connections**

AC input is an IEC-60320 C13 inlet.

DC output is an [Anderson](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Anderson_connector) [SBS50-BRN](http://www.andersonpower.com/us/en/products/sbs/sbs-50.aspx), but it seems to be a narrower pin pitch with no center data pin set.

CANbus signal interface is a JAE MX23A18NF1 connector (applies to the Calex, not the Mean Wells!)

| Pin | Function |
| --- | --- |
| 4 | CAN ground |
| 5 | CAN +5V power |
| 6 | CAN Dominant Low |
| 7 | CAN Dominant High |
| 10 | ob\_charger\_attached\_n [charger\_attached] |
| 11 | ob\_charger\_attached\_n [charger\_attached] |
| 12 | charger\_en\_0 [charger\_en\_n] |
| 13 | ob\_charger\_ref\_0 [charger\_gnd\_ref] |

**CANbus wiring**

Adapted from an examination of the wiring on a 2014 SR: [Onboard charger wiring for 2014 and 2015+](http://electricmotorcycleforum.com/boards/index.php?topic=6167) for the Calex.

When the onboard charger is plugged in and powered on the onboard charger pushes:

- 5V and 48mA through the Charger attached Pin #11.
- 5V and 26mA through the Charger enabled Pin #12.

The 5V ground reference is Pin #13 which is battery negative.

With this knowledge, another onboard charger solution can be wired to function as follows:

1. Run a separate circuit that when triggered pushes 5V ~50mA through pin#11 (attached charger) with the other end of the 5V circuit connected to the battery negative pin #13.
2. When this is triggered, the bike shows the battery state of charge % and charge time remaining, closes the contactor and allows charging - through the accessory charging port, the onboard charger port or via the Sevcon battery terminals for high power charging.
3. Upon completion of charging, the 5V can be switched off and the charge level and time remaining switch off and the contactor opens just as with the onboard charger.
4. The bike can be keyed on and ridden away as normal.

Using this method there is no need to leave the bike on when charging via the accessory charging port or the controller battery-side cables, or if you are using the [accessory charging port](#Accessory_Charging_Port) without triggering the auxiliary pin on the accessory charging port's Anderson SBS75XBRN.

**NOTE**

For 2015 onwards, the charger install uses additional wiring which may have a different approach using CAN signals, so it may require a different approach.

#### [Charger Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Calex_Charger_Replacement)

Since some generations of Calex chargers seem to develop faults relatively often, being able to replace a charger on one's own might save someone a lot of grief who doesn't live near a dealer.

**Video Guide**

[How to Remove the Zero's Onboard Charger by NewZeroLand on YouTube](https://www.youtube.com/watch?v=DFHQgTOMxO8) shows very clearly how to remove the charger from his Zero SR.

**Notes**

Adapted from [these instructions](http://electricmotorcycleforum.com/boards/index.php?topic=4424.msg28648#msg28648).

Possibly JAE MX23A18NF1 or MX23A18NF3 for harness connection [MX23A18SF1 (datasheet via Mouser)](https://www.mouser.com/datasheet/2/206/B-0094-2E_MX23A-1132557.pdf)

Charging enable hack (by [EMF user Liveforphysics](http://electricmotorcycleforum.com/boards/index.php?action=profile;u=1531))

![Zero Charger Enable At Harness](../images/LW_ZeroChargerEnableAtHarness_2018-09-25.jpg) *Zero Charger Enable At Harness*

**Tools**

- 3mm Allen key.

**Steps**

1. Unplug the motorcycle, and key it off. Wait for at least 10 minutes to ensure any residual charge has dissipated.
2. [Remove the lower plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lower_Plastics_Removal).
3. [Belly Pan Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belly_Pan_Removal)

   Unbolt the belly pan (2 rows of 4 3mm Allen head bolts on each side of the pan, and 2 smaller bolts) and remove it.
4. Unplug the wiring at the rear of the charger area.

   There are three plugs (looking left to right at the rear of the charger):

   - One on the AC end of things that's bolted to the bike (your charge plug)
   - The comms connector (enable signal, CAN comms etc...)
   - One plug on the DC side that goes up to the charge wiring harness.
   1. The comms plug just has a tab; push in the tab and pull that one out.

      Both of the other plugs are really difficult.
   2. Removing the DC plug.

      The plug is an [Anderson](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Anderson_connector) [SBS50-BRN](http://www.andersonpower.com/us/en/products/sbs/sbs-50.aspx), but it seems to be a narrower pin pitch with no center data pin set.

      The DC plug is located in front of the motor against the back side of the battery on the bike's right.
   3. The cables are tucked up between the battery and a frame member, so cut the zip ties (including the zip tie holding the plugs together) and pull the plastic zip-tie mount clips on the lower half of the cable going to the charger.
   4. Pull down on the charger side of the connector from the bottom while pulling up on the top connector.

      Sometimes this requires a "flesh donation" to the motor, so covering the motor with a rag would be smart.
   5. Pull the terminals out of the plug housing (see [Anderson disassembly](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Anderson_connector)), and pull it down thru the hole between the motor and frame.
   6. Removing the AC plug.

      It loops up under the seat and is zip tied on in a handful of places.

      There are two small bolts on the backside that are difficult to reach, so use a decent set of hex drivers with handles.
   7. There is a fuse holder plug that connects the ground to (somewhere...).

      Squeeze some tabs to get the green locking piece out.

      Then squeeze more tabs to get the plug apart.
5. Now with the cables out, use the 3mm Allen key to loosen (but not remove) the 6 bolts on the tabs holding it up.
6. Remove the charger to the side (recommend the right side) by removing the 3 bolts on the side intended for removal.

   On removing the last bolt, support the charger so it doesn't fall out, and carry it to the ground or elsewhere.
7. Remove the remaining 3 bolts using the 3mm Allen key if not installing a new charger.

**Assembly**

- Assembly is the reverse of disassembly! Really.

**Suggestion**

You can extended the DC wires on the replacement Calex charger, and put the plug set sideways, and up higher to make it easier to get at.

### [Main Bike Board](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board)

![2016 Zero MBB Front](../images/2016_Zero_MBB_Front.png) *2016 Zero MBB Front*

![2016 Zero MBB Back](../images/2016_Zero_MBB_Back.png) *2016 Zero MBB Back*

The Main Bike Board (MBB) controls the overall system, implements safety interlocks, and directs the controller.

It is also the entry point for configuring these systems, performing diagnostics, and examining operational events.

When referring to "the firmware", or "the logs", people are referring to this board primarily, and possibly the BMS.

It is enclosed within a fully-potted plastic-like container with multi-pin connectors along the top side.

**Location (S Platform)**

Below the front area of the seat under cable runs.

It is located aft of (and above) the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) with a bracket sandwiched between them.

![Board Plate Mounting Bracket (Left)](../images/2017-S-Frame_-_Board_Mounting_Plate_Left_Bracket.png) *Board Plate Mounting Bracket (Left)*

![Board Plate Mounting Bracket (Right)](../images/2017-S-Frame_-_Board_Mounting_Plate_Right_Bracket.png) *Board Plate Mounting Bracket (Right)*

**Location (X Platform)**

Below the front modular battery (or front half of a longbrick battery) in the triangular bay above the controller.

**Mounting (S Platform)**

Two socket head bolts with washers fasten the enclosure to a vertical plate.

The bolts enter the plate in the forward direction but offer very limited clearance for manipulating them.

**NOTE:** on the right, the cables from the controller to the motor run past.

A very small angled 3mm Allen Key wrench is best for unmounting the board.

**[Diagnostics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console)**

When using the OBD2 port, the board's application firmware supplies the interactive [console](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console).

[Playing with the 2012 MBB](http://electricmotorcycleforum.com/boards/index.php?topic=3057) shows Doctorbass' transcript using 2012 firmware.

- 2013 models' interface differs quite a bit from this but the general logic and experience are the same.

**Protections**

The board appears to be permanently sealed and potted within the enclosure to protect it from dust and a certain amount of moisture ingress.

**Interlock Troubleshooting**

Use careful electrical isolation measures when troubleshooting electrical switches used as inputs for interlocks enforced by the firmware.

**Replacement**

The board must have its firmware setup specific to the bike in question.

Major firmware difference exist across model years such that the firmware binary in question must be selected to prevent major problems on replacement.

- **NOTE:** *Apparently* only the manufacturer can perform this provisioning (probably imaging the base kernel, userland, and application-container management).

A dealer must select the correct and latest applicable *application* firmware to apply to the bike per its basic parameters:

- Year
- Model
- Battery configuration

Information from the bike's [VIN](https://web.archive.org/web/2025/https://zeromanual.com/wiki/VIN_Guide) is necessary to select the right programming by the dealer or manufacturer.

This information may not be sufficient, if it requires coding in the presence of a [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank) or [Charge Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Charge_Tank).

The board settings require model information to be set per above, and the BMS must agree about this information.

#### [Main Bike Board Limitations](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board/Limitations)

The board design is very modest and seems to prioritize light weight and simplicity over robustness.

Take as much care as possible when troubleshooting in and around this module.

A professional-grade application of dielectric grease around the connectors seems advisable.

- **NOTE:** Ensure that the entire connector and pins are clean and dry before applying.

**Performance and Lockup**

The board communicates with the bike's other systems via [CAN Bus](https://en.wikipedia.org/wiki/CAN_Bus), which is a 2-wire [Multi-master bus](https://en.wikipedia.org/wiki/Multi-master_bus).

- This means that multiple nodes on the bus must initiate a transfer.

The board also has limited memory, I/O dispatching, and computational performance.

- So, it can get clogged with requests for data outside its designed parameters.
- So, running any telemetry while in drive mode through the OBD-II serial console or using the Bluetooth transmitter will meaningfully increase the load on the board.

  In some cases prevent it from acting on rider inputs, including safety interlocks like the cutout switch or kickstand interlocks.

Reportedly, 2017 and newer models have increased performance and doubled memory capacity.

- This enables an onboard upgrade with an atomic swap of versions by holding new and old firmware versions simultaneously.
- There's no known means of using these in older models.

**Electrical Vulnerability**

The circuits connected to the pins seem to lack significant protection against shorting faults, which could be a source of breakages while dealing with connected systems.

**OBD-II Serial Output**

The use of the non-standard OBD-II port most easily draws power from a very limited internal circuit.

The OBD-II port as a result is typically not usable over a long cable without an external power supply and good quality connections.

#### [Main Bike Board Connections](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board/Connections)

The board has a 34-pin and 40-pin connector exposed through the top of the enclosure, making them relatively accessible and a way to identify the component.

Both are made by [JAE Electronics](http://www.jaeusa.com/).

![2016 Zero MBB Top](../images/2016_Zero_MBB_Top.png) *2016 Zero MBB Top*

| Connector | Harness-side | MBB-side | Notes |
| --- | --- | --- | --- |
| 34-pin connector "MBB 1" | [JAE Electronics MX23A34SF1](https://www.mouser.com/ProductDetail/JAE-Electronics/MX23A34SF1/) | [JAE Electronics MX34A34NF1](https://www.mouser.com/ProductDetail/JAE-Electronics/MX23A34NF1/). | ![Harness-side pinout; MBB side mirrored](../images/MBB_pins.png) *Harness-side pinout; MBB side mirrored* <br> ![2013 MBB 1 connector Wiring Diagram image](../images/Mbb-1-connector.png) *2013 MBB 1 connector Wiring Diagram image* |
| 40-pin connector "MBB 2" | [JAE Electronics MX23A40SF1](https://www.mouser.com/ProductDetail/JAE-Electronics/MX23A40SF1/) | [JAE Electronics MX34A40NF1](https://www.mouser.com/ProductDetail/JAE-Electronics/MX23A40NF1/) | ![2013 MBB 2 connector Wiring Diagram image](../images/Mbb-2-connector.png) *2013 MBB 2 connector Wiring Diagram image* |

| Component | Function | Wire | MBB Pin | Role |
| --- | --- | --- | --- | --- |
| [Kickstand Switch](#Kickstand_Switch) | Safety Interlock | Red (2013) 20AWG | 27 | Colors are different for 2016 models: |
| 〃 | 〃 | Orange (2013) (black) 20AWG | 12 | Blue (5v power), Pinkish Red (measure signal TODO), Black. <br> Do **not** short these directly. That is not how you bypass. |
| 〃 | 〃 | Yellow (2013) (black) 20AWG | 11 | [Kickstand Switch](#Kickstand_Switch) |
| [Kill Switch](#Kill_Switch) | Safety Interlock | Red 20AWG | 23 |  |
| 〃 | 〃 | White 20AWG | 24 |  |

| Component | Function | Wire | MBB Pin | Function | Notes |
| --- | --- | --- | --- | --- | --- |
| DC-DC Converter | Enable Signal | Orange (Red) 18AWG | 21 (2013) <br> 20 (2015) |  |  |

### [Charging Control Unit](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Control_Unit)

The Charging Control Unit (CCU) on Meanwell-charger-equipped models (all 2013 and the 2014FX) collects battery temperature sensor data, battery voltage, and charger DC voltage to decide on whether to open or close the [contactor](#Contactor). It also manages the Meanwell [onboard charger](#Charger) which has no CANBus connection or programmability, so when the programmable Calex charger was introduced, the CCU's functions were moved to direct BMS/MBB management.

![CCU top](../images/CCU-top.JPG) *CCU top*

![CCU back](../images/CCU-back.png) *CCU back*

![CCU front](../images/CCU-front.png) *CCU front*

**Connectors**

CCU 18-pin connector: [JAE Electronics MX23A18SF1](http://www.mouser.com/ProductDetail/JAE-Electronics/MX23A18SF1/?qs=sGAEpiMZZMs7eK6h2EBtKkAz7jnNYZmagRPFVYhCTJM%3d)

![2013 CCU Connector diagram](../images/Ccu-connector.png)

![Ccu-connector-schem.png](../images/Ccu-connector-schem.png)

**TODO**

more from Burton's post here: [Re: 2013 S 11.4 quick charger build](http://electricmotorcycleforum.com/boards/index.php?topic=3987.msg25494#msg25494)

The contactor protects the battery against faults. It is analogous to a circuit breaker. The CCU directs it.

2012-2013 models exhibited behavior where the BMS in certain situations yielded a "contactor welded shut" condition that require dealer servicing. Later model years fail more safely (open).

2014+ models do not have a CCU, and the BMS directly controls the contactor and onboard charger.

**Location**

Under the seat in front of the [MBB](#Main_Bike_Board) with the connections mounted on top.

**Limits**

The CCU terminals are not designed for high amperage currents. Presumably, anything above the 2013's intended 30A charging limit could damage the CCU or trigger the contactor opening.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | This is always energized. Any exposure of this at any time will risk direct contact with battery terminals that could result in injury or equipment damage. <br> **DO NOT UNCOVER** this without professional-level care! |

If you are in a remote location, and have trouble with a contactor unit not closing without any indication of a particular condition that interlocks it in the BMS, a little mild mechanical agitation (while the vehicle is keyed off) against the top surface with a rubber mallet might loosen it.

### [DC-DC 12V converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter)

The DC-DC 12V converter is a solid state switching power DC step-down converter designed to produce low voltage DC power from the pack voltage.

The converters mentioned here are used on [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) and [Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3) models.

| Years | Platform | Manufacturer | Model | Replacement Options |
| --- | --- | --- | --- | --- |
| 2013-2014 | S and X | Sevcon | [Sevcon DC-DC 300W converter](http://www.sevcon.com/products/dcdc-converters/dcdc-300w/) | OEM or [via Thunderstruck Motors](http://www.thunderstruck-ev.com/sevcon-72-80v-dc-dc-en.html) <br> - **NOTE:** Select the 300W model! connector hardware is an extra |
| 2015+ | 〃 | 〃 | [Sevcon DC-DC 500W converter](http://www.sevcon.com/products/dcdc-converters/dcdc-500w/) | OEM or [via Thunderstruck Motors](http://www.thunderstruck-ev.com/sevcon-72-80v-dc-dc-en.html) <br> - **NOTE:** Select the 500W model! connector hardware is an extra |

**Appearance**

It's about the size of a long box of soap with a black surface, but for 2013-2014 models will be covered entirely with Nashua aluminum ducting tape, so will appear silver.

| | | |
| --- | --- | --- |
| ![500W Sevcon DC-DC converter - top](../images/DC-DC_Sevcon_500W_Converter_-_1.png) *500W Sevcon DC-DC converter - top* | ![500W Sevcon DC-DC converter - connector](../images/DC-DC_Sevcon_500W_Converter_-_2.png) *500W Sevcon DC-DC converter - connector* <br> ![500W Sevcon DC-DC converter - connector side](../images/DC-DC_Sevcon_500W_Converter_-_3.png) *500W Sevcon DC-DC converter - connector side* | ![500W Sevcon DC-DC converter - side](../images/DC-DC_Sevcon_500W_Converter_-_4.png) *500W Sevcon DC-DC converter - side* <br> ![500W Sevcon DC-DC converter - backplate (upside down)](../images/DC-DC_Sevcon_500W_Converter_-_5.png) *500W Sevcon DC-DC converter - backplate (upside down)* <br> ![500W Sevcon DC-DC converter - backplate (as installed)](../images/DC-DC_Sevcon_500W_Converter_-_6.png) *500W Sevcon DC-DC converter - backplate (as installed)* |

**[SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) Location**

Below the front of the seat under cable runs, between the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) (separated by a bracket) and the back of the battery frame area.

[Quick and dirty illustrative video of how to find and access the converter](https://www.youtube.com/watch?v=yig2RtRuIoY)

**[XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform) Location**

Below the removable battery compartment. See [our FX teardown layout guide](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Electrical_Routing).

**[FST Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FST_Platform) Location**

Inside the tank, on the right of the bin, on the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FST_Platform/Board_Mounting_Plate).

**Protections**

- Ingress: IP67
- Short circuit overload
- Reverse polarity
- Fully isolated
- Can parallel with diode safeguard

**Mounting**

The Sevcon 500W DC-DC converter is mounted to its own baseplate via 4 Torx T10 cap head screws and there are 3 additional Torx T15 cap head screws in the middle.

The Sevcon baseplate is then bolted to Zero's [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate) with 4 10mm hex head bolts which have 6mm outer diameter, 16mm length, and 1mm pitch.

**Removal**

1. [Remove](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Board_Mounting_Plate_Removal) the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate).
2. Remove the converter from the board using a 10mm hex socket wrench.
3. Disconnect the connector if appropriate.

**Installation**

1. Attach the converter to the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate) with a 10mm hex socket wrench.
2. Install the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate) with the converter back into the bike.

**Connections**

There is a 5-pin connector controlling the converter, facing the left as installed on the bike, connected as follows:

| Pin | Function | Measurement | Component | Years | Wire | MBB Pin | Illustration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Enable signal | Battery voltage when key is on | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | 2013 | Orange (Red) 18AWG | 21 | ![Dc-dc-connector.png](../images/Dc-dc-connector.png) |
| 〃 | 〃 | 〃 | 〃 | 2015 | 〃 | 20 | 〃 |
| 2 | Input (Positive) | 116V | [Battery](#Battery) | 2013 | Orange (Blue) 16AWG | 7 | 〃 |
| 3 | Input (Negative) | 〃 | 〃 | 2013 | Orange (Black) 20AWG | 5 | 〃 |
| 4 | Output (Positive) | 13.5V | [Fuse Block](#Fuse_Block) | 2013 | Blue (16AWG, 14AWG) wires |  | 〃 |
| 5 | Output (Negative/Ground) | 〃 | [12V return conduits](#Routing) | 2013 | Black 10AWG |  | 〃 |

**Output**

It is configured to output 13.5V DC; usually produces ~13.8V DC.

There is very little ripple that is typical of a gas-power motorcycle's alternator-driven DC supply.

Capacity is 300W (20-25A) for pre-2015 bikes and 500W (35-40A) for 2015+ models, with most of that excess needed to run ABS pumps, etc.

**Operation**

The input side is always-on DC from the battery, upstream of the contactor.

This is the best place to tap for an always-on power supply.

The converter is enabled by a 12V signal from the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB).

**Environmental Vulnerability**

- The Sevcon DC-DC converter is rated to IP67 for intrusion protection and seems very robust as such.
- However, the connector is not sealed, faces the left side of the inside of the frame arms with not much splash protection from beneath; on 2015+ models, it is also vulnerable to debris and splash impact from the rear near the motor and belt.
- No sealed connector option is currently available for Sevcon's DC-DC converter models that Zero uses.
- Connector looseness could age and wear the converter prematurely due to sporadic voltage input or output changes.
- Leakage across pins could cause the enable signal to activate inadvertently.

**Connector Inspection**

Try to inspect the pins' tabs to ensure they are in the right shape to clamp that enable pin securely.

The connector is not well-sealed, and the pins are too easy to bend into not-connecting if there's any tension/tugging on the wires.

If the connector seems grimy, remove and clean it while de-energized; then apply grease once dry before re-seating it.

Test the connector before fully re-assembling the bike.

**Failure to De-energize Condition**

The converter can fail in a way where it shorts its enable line and will not turn off even if the bike is keyed off.

- If this condition happens in rain:
  1. Let the bike dry out until it clears.
  2. Attempt a dielectric grease application to the inputs while de-energized.

If the DC system output disappears:

- Check DC voltage upstream of the fuse block in case the fuse block is faulty.
- Check the continuity and snugness of the connectors and pins.
- Check for the enable signal from the MBB

  Continuity: < 1Ω between pins.

  Not shorted to B+?: > 151kΩ from pin 20 to pin 7.

  Not shorted to ground?: > 1MΩ from pin 20 to 18.

**Protection Recommendations**

- Splash protection around the left-side's connector from all sides is worth considering.

**References**

[Re: My DC-DC converter has died again, local dealer has gone bust](http://electricmotorcycleforum.com/boards/index.php?topic=6904.msg57973#msg57973)

[Re: A puddle, some rain and some problems](http://electricmotorcycleforum.com/boards/index.php?topic=7041)

### Power Harness

The power cables and signal wiring that connects the MBB to the BMS units intended for that platform and year are collectively bundled and referred to as a “power harness”.

#### [Loopback Blanking Plug](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loopback_Blanking_Plug)

The loopback blanking plug is a Zero electrical connector cap that wires two pins together in a *[loopback](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS_CANBus_Loopback)* circuit.

This meant to emulate a basic connectivity feature for the BMS1 connection so that the vehicle's CAN Bus can operate properly.

If you own a non-longbrick X platform model or an S-platform model with a [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank), retain this blanking plug in case your second BMS fails to connect or issues errors that prevent your motorcycle from operating.

#### [Loopback](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS_CANBus_Loopback)

BMS CANBus loopback is a function of the built-in cable communications support for the [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank) or the second [Power Pack Module](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module) in a non-longbrick X platform model (labeled *BMS1* by the MBB).

The cabling ends in a multi-pin connector and should either:

1. Terminate with a [Loopback Blanking Plug](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loopback_Blanking_Plug) that wires two pins together in a *loopback* circuit.
2. Connect to a [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank)'s corresponding communications cable.

If one of the above conditions do not hold, the MBB is configured to issue [error code 35](Error_Codes.md#35 "Error Codes").

It is unconfirmed what purpose the loopback mechanism serves.

*Hypothesis:* This is a hardware debugging mechanism for a loose connector.

### [Firmware Update](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Firmware_Update)

Firmware update refers to the process of acquiring and installing newer [firmware versions](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Firmware_Versions) from Zero onto the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB), [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS), and the motor controller.

**Dealership Updates**

Firmware update for pre-2017 models must be performed by a dealership with a license with Zero and the hardware kit to connect a Windows computer to the motorcycle's data ports (OBD-II, the BMS serial port, and the Sevcon 34-pin connector).

**Mobile App Self-Service Updates**

On 2017 and newer Zeros, it's possible for the user to [upgrade the firmware via the Zero Motorcycles mobile app](Official_Mobile_Application.md#Firmware_Update "Official Mobile Application").

### [Firmware Versions](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Firmware_Versions)

Using the Zero App to download the logs, and Phreak's Log Parser Utility ([forum](http://electricmotorcycleforum.com/boards/index.php?topic=5020.0), [Github](https://github.com/KimBurgess/zero-log-parser), [online](http://home.hasslers.net/zerologparser/)), different users have reported the latest firmware versions to be:

|  | MBB |  | BMS |  |
| --- | --- | --- | --- | --- |
| Board Year | Revision | Version | Revision | Version |
| 2013 | 1 | 67 |  |  |
| 2014 | 1 | 44 | 1 | 43 |
| 2015 | 3 | 25 |  |  |
| 2016 | 3 | 51 | 3 | 39 |
| 2017 | 12 |  | 21 |  |

The online log parser has a list of the most recent firmwares that have been uploaded to the server:
[Latest Firmware Versions](http://home.hasslers.net/zerologparser/firmware-summary.php)

Feel free to update this section as you discover new available updates.

| Version Changes |  |  |  |
| --- | --- | --- | --- |
| Component | Version | Release Date | Notes |
| BMS |  |  |  |
| MBB | 48 | spring 2017 |  |
| 〃 | 49-51 | 49 Build Date: 06Jul2016 <br> 51 Build Date: 25Apr2017 | Confirmed: SoC improvements, particularly for pre-2016 model years. <br> Observed: 2016 SoC is significantly more pessimistic in v51 than in v49. <br> Guess: Throttle remapping to a smoother roll-on curve. <br> Guess: Regen seems to apply more broadly. |

**Problems**

- Firmware mismatch problems (bms on power tank versus ZF pack)
- SoC problems
- Which versions are known safe?
- Observed changes
- Differences by year/model
- MBB
- BMS0
- BMS1

**Upgrading Firmware**

As of 2017, Zero models are capable of performing remote firmware updates by the customer [using the mobile app](#Using_Mobile_App).

Apparently this doesn't transfer to older models because the older boards did not have enough storage space to perform an atomic/reversible update.

This means holding both firmware versions and being able to toggle which version to use.

So, if anything goes wrong with a firmware update, the system can roll back to the previous version without requiring a dealer visit.

**ChangeLog**

Zero Motorcycles on their website now [lists changes of Zero Motorcycles vehicle firmware](https://www.zeromotorcycles.com/owner-resources/firmware/)

## Battery

The following guidance includes advice adapted from [MostlyBonkers' research summary](http://electricmotorcycleforum.com/boards/index.php?topic=4280.0) and [Battery Notes from a Farasis Engineer](http://electricmotorcycleforum.com/boards/index.php?topic=5314).

### [Battery Concepts](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Concepts)

**Basic Concepts**

Metaphorically speaking, think of a river and a reservoir.

**Volts**

water pressure.

**Amps**

volume of water flowing.

**Charge (Kwh)**

how much water is behind the dam.

**Power (kW)**

the rate at which water is flowing.

### [Charge Tips](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Charge_Tips)

Generally, refer to the [Charger Operation](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Calex_Charger/Operation) section, but for battery concerns, the following are relevant:

1. If you run your bike to empty, do your best to give it at least a partial charge (ideally to 40-50%) as soon as you can.
2. Charge and discharge your bike freely and at your convenience.
3. Don't worry about keeping the bike topped up, like standard car batteries.
4. Don't feel you have to run the bike to empty before re-charging; it's fine to charge if you've only used 10%, for example.
5. If you can afford extra chargers to reduce charging time, Zero's fast chargers won't hurt the batteries.
6. Use the bike as much as you can. If you aren't using it for a regular commute or aren't lucky enough to have the freedom to ride regularly then it will work out a lot cheaper to own a conventional motorbike.
7. Zero's engineers have done the work to ensure a long service life from their battery packs and have backed it up with a five year warranty with the 2014 model range onwards. That should be enough to drop any anxiety you may have and just concentrate on enjoying the bike.

### [Battery Capacity](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Capacity)

[Battery capacity](https://en.wikipedia.org/wiki/Electric_battery#Capacity_and_discharge) is a measure of the charge a battery can deliver at an intended voltage.

Cells themselves are usually rated for a current amount delivered over an interval of time (going from maximum voltage to a rated minimum).

Batteries as banks of cells aggregate that measure across the cells.

Because of a number of factors including *internal resistance*, a higher discharge rate effectively *lowers* the usable capacity of the battery during that cycle.

This variance in the usable capacity of the battery has meaning for how an electric motorcycle performs with different riding styles.

Normally, the energy a battery can store is estimated by taking nominal voltage (V) times the current capacity of the battery's cells (Ah) = the energy delivery capacity (Wh) (divide by 1000 for kWh).

```
PackVoltagenominal (V) × CellCapacity (Ah) = EnergyCapacity (Wh)
```

However, based on industry convention, Zero calculates battery energy (the kWh) by taking the maximum voltage the battery has at 100% capacity times the capacity in Ah, instead of nominal voltage.

**Maximum Voltage**

*Maximum voltage* is only present at the beginning of discharge when it is full, and then it drops (nonlinearly).

**Nominal Voltage**

The *nominal voltage* is like the average voltage the battery over the entire discharge range.

The average is the voltage measured at the battery terminal when it has 50% charge state and is disconnected from any load.

For example, the 2013 S has **100Ah** and a nominal **102V**: the total energy the battery has is:

```
102V × 100Ah = 10200Wh = 10.2kWh
```

But if you use maximum battery voltage you get:

```
116V × 100Ah = 11600Wh = 11.6kWh
```

This also applies when adding a power tank, confusing customers about the official rating versus what the mobile application reports.

Regardless of this complexity of measurement, Zero's range figures appear reliable in the general context of the test conditions.

### [Cells](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Cells)

The current manufacturer of cells for Zero's power packs is [Farasis](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Farasis) who are supplying [pouch cells](http://www.farasis.com/solutions/cells/) for the 2013+ model range ([Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) and [Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3)).

**NMC Cell Chemistry**

The chemistry used is **Lithium Nickel Manganese Cobalt**: LiNiMnCoO2 ("NMC" or other rearrangements of those letters).

NMC is a relatively new battery chemistry which *differs from* the Li-cobalt chemistry we are familiar with from mobile phone batteries and laptops.

While Li-cobalt has a higher energy density than NMC (storage capacity per kilogram), it doesn't cycle as well and ages quicker.

That's fine for a mobile phone that is likely to be obsolete after 2-3 years, but not for an electric bike.

The automotive-grade NMC cells that Farasis supply should easily satisfy the requirements of the five year warranty that Zero are providing with their current Z-Force battery packs.

It seems they should last 8-10 years if they aren't abused.

Even if you start to notice some significant deterioration after five years, the rate at which battery technology is progressing means that you should be able to buy a new battery pack with much better capacity (range) than the original for less money.

|  |  |  |  |  |  | Voltage |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Years | Form | Manufacturer | Model | Datasheet | Capacity | Minimum | Nominal | Maximum | Dimensions |
| 2009-2011 | cylindrical | [Molicel](http://www.molicel.com/ca/) | [IMR-26700A](http://www.molicel.com/hq/product/products11.html) | [Molicel 26700](http://wamtechnik.pl/files/specs/645.pdf) [[13]](https://evmc2.files.wordpress.com/2013/12/imr26700.pdf) [[14]](https://master-instruments.com.au/products/60681/IMR26700A.html) | 2.9Ah | 2.5V | 3.8V | 4.2V±50mV | 26.4mm ⌀ × 70mm |
| 2012 | pouch | [EIG](http://www.eigbattery.com) | [EIG C020](http://www.eigbattery.com/_eng/designer/skin/02/01_03.asp) | [EIG NCM C020](http://www.eigbattery.com/_eng/developer/m_product_data_set/download.asp?file_nm=EIG_NCM_C020_Data-sheet_APR2016.PDF) | 20Ah | 2.5V | 3.65V | 4.15V | 130mm × 217mm × 7.2mm |
| 2013-2014 | 〃 | [Farasis](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Farasis) | Farasis 25Ah | [Farasis IMP06160230P25A 25Ah](http://www.cdiweb.com/datasheets/ctc-battery/FEI-DataSheet-IMP06160230P25A-Pouch-25Ah-v5.pdf) or [alt](https://evmc2.files.wordpress.com/2013/12/fei-datasheet-imp06160230p25a-pouch-25ah-v5.pdf) | 25Ah | 2.0V | 3.65V | 4.15-4.20V | 161mm × 230mm × 6mm |
| 2015 | 〃 | 〃 | Farasis 27Ah | 〃 | 27Ah (25Ah label) | 〃 | 〃 | 〃 | 161mm × 230mm × 6mm |
| 2016-2017 | 〃 | 〃 | Farasis 29Ah | 〃 | 29Ah (28Ah label) | 〃 | 〃 | 〃 | 160mm × 230mm × 6mm |
| 2018 | 〃 | 〃 | [Farasis 32Ah](https://chargedevs.com/newswire/new-farasis-pouch-cell-balances-power-and-energy-density/) | 〃 | 32Ah (? label) | 〃 | 〃 | 〃 | 160mm × 230mm × 6mm |

**Farasis Claims**

Per Farasis engineers and industry professionals:

**25Ah**

A solid cell, and are Farasis's oldest chemistry design.

They are a manganese-rich cathode (NMC) 25Ah cell with excellent cycle life, and acceptable [C-rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate).

**27Ah**

An adaptation of the 25Ah cell chemistry with thinner foils and more of them.

This means that there is more active materiel (more capacity) but less conductive path to get that capacity in and out.

So for the slow discharge S/DS bikes, you get more capacity, but they are lower C rate, and cannot handle being used in the FX platform.

**29Ah**

Higher discharge rate (peak and continuous) than the 25Ah cell.

More capacity than the 27Ah cell (especially at higher [C rates](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate)/cooler temperatures).

**32Ah**

10% capacity improvement and very likely lower internal resistance.

Internal weight savings and better cooling are inferred.

|  | Discharge |  |  | Charge |
| --- | --- | --- | --- | --- |
| Cell | Continuous | Peak (10sec) | Max Burst | Maximum |
| 25Ah | 4C (100A) | 7C (175A) | 400A | 1C (25A) |

**References**

[2014 ZERO BATTERY CHEMISTRY (Z-FORCE® POWER TANK SECRET SAUCE)](https://evmc2.wordpress.com/2013/12/01/2014-zero-battery-chemistry-z-force-power-tank-secret-sauce/)

[DoctorBass on Endless Sphere: Zero Motorcycles BATTERY for your E-projects!!](https://endless-sphere.com/forums/viewtopic.php?t=87997)

[Charged EVs: New (32Ah) Farasis lithium-ion pouch cell balances power and energy density](https://chargedevs.com/newswire/new-farasis-pouch-cell-balances-power-and-energy-density/)

[Battery notes from a Farasis Engineer. @ ElectricMotorcyleForum](https://electricmotorcycleforum.com/boards/index.php?topic=5314.0)

### [Cell Arrangement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Cell_Arrangement)

Cell arrangement (also *battery arrangement* or *battery configuration*) refers to how the cells are grouped to provide power with sufficient current and voltage output for the application.

- *Series* arrangements raise pack voltage
- *Parallel* arrangements increase pack current capacity, as well as balance cells if they are cross-connected.

**Notation**

See [Battery Cell Arrangement Notation](http://liionbms.com/php/wp_series_parallel.php) to understand how Zero's battery cell arrangements are described.

| Cell | Voltage | Series | Pack Voltage | Years | Platform |  | Configuration |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Molicel 26700 | 3.8V | 14 <br> 7⨉2s banks | 48V (min) <br> 53V (nominal) ≈ 3.8V × 14 <br> 58V (listed/max) | 2009 | S | 14s24p | [Monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) (12 or 24 parallel) |
| 〃 | 〃 | 〃 | 〃 | 2010-2011 | X | 14s12p | 〃 |
| 〃 | 〃 | 〃 | 〃 | 〃 | S | 14s24p | 〃 |
| [EIG C020](http://www.eigbattery.com/_eng/designer/skin/02/01_03.asp) 20Ah | 3.65V | 18 | [65.7V](http://electricmotorcycleforum.com/boards/index.php?topic=6630.msg56388#msg56388) (nominal) ≈ 3.65V × 18 <br> [74.7V](http://electricmotorcycleforum.com/boards/index.php?topic=3481.msg19765#msg19765) (max) | 2012 | X | 18s1p | 1 module |
| 〃 | 〃 | 〃 | 〃 | 〃 | S | 18s2p or 18s3p | 2 or 3-brick [monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) |
| [Farasis 25Ah](http://www.cdiweb.com/datasheets/ctc-battery/FEI-DataSheet-IMP06160230P25A-Pouch-25Ah-v5.pdf) | 〃 | 28 | 116V (max) <br> 102V (nominal) ≈ 3.65V × 28 <br> 84V (min) | 2013-2014 | XMX | 28s1p | 1-2 removable [modules](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module) |
| 〃 | 〃 | 〃 | 〃 | 〃 | SDS | 28s3p or 28s4p | 3 or 4-brick [monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) |
| 〃 | 〃 | 〃 | 〃 | 2015 | XMX | 28s1p | 1-2 removable [modules](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module) |
| [Farasis 27Ah](http://www.cdiweb.com/datasheets/ctc-battery/FEI-DataSheet-IMP06160230P25A-Pouch-25Ah-v5.pdf) | 〃 | 〃 | 〃 | 〃 | SDS | 28s3p or 28s4p | 3 or 4-brick [monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) |
| Farasis 29Ah | 〃 | 〃 | 〃 | 2016 | XMX | 28s1p | 1-2 removable [modules](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module) |
| 〃 | 〃 | 〃 | 〃 | 〃 | SDS | 28s3p or 28s4p | 3 or 4-brick [monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) |
| 〃 | 〃 | 〃 | 〃 | 2017-present | XMX | 28s2p | [Long Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Long_Brick) (fixed), or 1-2 removable [modules](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module) |
| 〃 | 〃 | 〃 | 〃 | 〃 | SDS | 28s2p or 28s4p | [Long Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Long_Brick) with storage, or 2x[Long Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Long_Brick) [monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) |

**References**

[2011 Zero S battery rebuild to Tesla cells](https://www.youtube.com/watch?v=NukSXWpbBsE) reveals Molicel construction for the 2009-2011 era.

[Zero Motorcycles BATTERY for your E-projects!! by DoctorBass](https://endless-sphere.com/forums/viewtopic.php?t=87997)

#### [Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Brick)

Zero arranges Farasis cells in 28-cell series in modular form, referred to as "bricks" because they're bathed in an epoxy after assembly. The brick configuration is "28s1p".

Both the [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank) and [Power Pack Module](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module) products encapsulate a single brick.

For the S platform 2014+ years, installing the [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank) changes a "4p" to a "5p" (and presumably "3p" to "4p" but this seems unlikely).

**Components and Weight**

28 cell ⨉ 485 g/cell = 29.9 lb

For 2015, each brick weighs 32 lb, implying 2.1 lbs for epoxy/etc.

**Dimensions**

8? x 7.5 x 9.75in (HxWxL)

**References**

[DoctorBass' repackaging of a 25Ah brick into two, length-wise](https://endless-sphere.com/forums/viewtopic.php?f=3&t=65764&hilit=battery#p994254) reveals some structure.

#### [Monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Monolith)

![Monolith technical rendering published in 2016](../images/2_monolith.png) *Monolith technical rendering published in 2016*

The term "monolith" refers to Zero's standard [Z-Force Power Pack](http://www.zeromotorcycles.com/technology/) sealed battery assembly with specific, fixed dimensions and a single [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) with fixed communication and power interface.

A monolith is designed to package up to 4 parallel bricks, described as "4-brick" or "28s4p", referring to 4 parallel stacks of 28 cells in series.

The 4p arrangement is a "full" arrangement: the monolith is split into 4 equal quadrants each fitting a brick.

A "3-brick" arrangement was available for 2013-2016 S and DS bikes, leaving the forward upper quadrant empty (presumably filled with lightweight but load-absorbing material).

**Interconnects**

An interconnect wiring system electrically connects each cell across bricks that is in the same position in the series.

- Interconnects minimize the complexity of cell balancing by ensuring that only 28 conductive connections are needed from the single [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) to keep cells balanced.
- Interconnects also ensure that a set of 3 or 4 cells are electrically able to balance a certain amount of load, reducing stress from imbalanced load variations while running.

Interconnects do seem to embody some specialized emergency fuse safeguards.

**Components and Weight**

32 lb/brick ⨉ 4 brick = 128 lb

The 4-brick monolith weight of 140 lb implies 12 lb for the base plate, BMS, dog house with contactor, current sensor, fuse, and connectors.

**Casing features**

- The front face has two holes for accessing the BMS indicators, I/O port, and reset buttons.
- The front face is also removable for servicing the BMS; within, the interconnects to the cells are on the left edge (as seen while facing the battery from the front); on the top edge are connections to CANBus communications and the external power bus.
- The trailing edge of the left side of the monolith casing features an arc cutout with two holes.

  This cutout accommodates/mounts a [CHAdeMO](https://web.archive.org/web/2025/https://zeromanual.com/wiki/CHAdeMO) charging inlet (and can adapt to a Type 1 or Type 2 J1772 inlet with some fabrication).

  Threaded inserts are included for the inlet mounting, sized for M5 bolts at 80mm distance from each other (center to center).

  Refer to [Yazaki's CHAdeMO connector manual](http://charge.yazaki-group.com/english/pdf/YPES-15-1407E.pdf) for details.
- The top rear module called the doghouse contains the contactor and sensors for operating the safety limits.

#### [Long Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Long_Brick)

The 2017 model year shifted Zero's battery assembly to a "half monolith" or "long brick" configuration containing the same number of cells as for 2 [bricks](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Brick).

A single [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) manages the cells in both stacks.

**Model Changes**

- The 2017 S and DS models offer a 2p arrangement using a single long brick arranged along the forward half of the monolith frame area.

  This configuration leaves the rear half of that area empty for a storage bin accessed from the side of the frame.

  The prior 3p configuration is no longer for sale, but can be created by adding a [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank).

  The long brick for this model does not have the same gapped casing that a Monolith has

  So, it is less insulated from cold but dissipates heat better.
- The 2017 [XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform) models are delivered by default with a non-removable long brick (aside from the [MMX Model](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MMX_Model)).

  They are available optionally with single removable bricks like prior model years for an additional cost of about $500.

**Design**

The long brick arrangement figures suggest that each brick aligns its cells with the other brick.

- Layout appears to be more efficient as a result.
- Interconnects between the bricks seem to be trivial and nearly-zero-resistance, improving cell life.
- There is unsupported speculation that 56s1p arrangement is a possible future evolutionary step as a result.

**Dimensions**

15" tall × 9 3/4" wide × 6 1/2" deep.

There will be some plastics on it with the contactor and bms inside that add about 2" to the height and 1" to the depth for about half of the height of the battery.

[Facebook comment for measurements](https://www.facebook.com/groups/zmcowners/permalink/3005387632863758/?comment_id=3005390942863427&reply_comment_id=3005421196193735)

**Long brick [Monoliths](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Monolith)**

For 2017 packs, made with "long bricks", the interconnects are extremely simple, only connecting two stacks which are aligned directly against each other.

2017 monoliths consist of two "long bricks" with simpler interconnects.

### [Battery Management System](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery_Management_System)

Zero's Battery Management System (BMS) consists of a proprietary board within the battery case to manage the cells.

![2016 BMS with potting](../images/BMS_with_potting_large.png) *2016 BMS with potting*

The same board model seems to be capable and used for both single-brick ([XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform)) bikes and power pack ([SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform)) bikes, given software configuration changes. The board appears to be OEM-designed and has revision numbers that indicate progression over time from the 2013 model line.

**Power Note**

This is the one power drain on the vehicle when it is completely turned off with no charging, but it draws a very minor amount of power like a "sleep" mode.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | The board is entirely solid state and not designed for fixing, only replacement. <br> Any damage to this board will disable the motorcycle. |

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | The board has full battery voltage inputs to it at all times. <br> Take extreme care to avoid connections that could short, arc, or ground. <br> Before accessing the BMS, first turn the bike off and disconnect charging. <br> This ensures that the contactor is open and you do not interact with the BMS while it performs a cel balancing operation. |

**Location (SDS Platform / Monolith)**

Behind the lower front face of the battery behind the front forks/wheel.

Remove the lower front body plastics and the front battery face to access the unit.

**Location (XMX Platform / Power Tank)**

Each separate brick has its own BMS inside the armored casing.

The long brick has one BMS module inside the armored casing.

**Revisions**

The BMS has changed layout over the years to match the monolith (particularly for long brick architecture) and increased in physical robustness and protections.

TODO identify those revisions and describe them.

**Protections**

The board is mounted with rubber vibration dampening.

The board is layered with a very thick coating ("dam and fill potting") to protect the components from moisture and shock damage.

The rubber pads covering reset buttons and LED indicator lights (for 2015+ models) have dielectric grease coating ([CP70](http://www.americansealantsinc.com/silicone-grease/) [datasheet](http://www.americansealantsinc.com/wp-content/files_mf/asi70pds.pdf)) those components.

- The covers are not there to make it waterproof, only to keep the dirt out of the grease.
- MY13 bikes had no grease. MY14 bikes had a different grease that did not age well, and [CP70](http://www.americansealantsinc.com/silicone-grease/) is worth applying to both MY13 and MY14.
- Maintain that coating and do not pressure wash the front of the battery casing to avoid damaging this board.

**Inspecting**

If the BMS stops working (no indication from the lights, no response to reset), the appropriate, non-warrantee-risking thing to do is take it to a dealer and they'll likely replace it under warrantee.

But if a dealer visit is difficult or there's an emergency, a visual inspection might inform what's going on (naturally, a bike that doesn't work feels like an emergency; use your judgement).

Basically, uncover the BMS and look for burned out components.

There is a large pin connector which may be loose, which would explain a loss of power to the BMS. Apparently this is very difficult to work with but can be re-attached carefully.

Don't loosen the BMS mounting without a very good reason - it's always connected to battery cell voltage by some pins on the side that run into the batter pack so a spark there might be damaging.

If you are going to lift off the BMS, take extreme care with the fasteners and dampeners to not drop them into the battery casing.

You'll also need to restore each and every fastener and dampener because the BMS mount prevents vibration damage.

**Diagnostics**

The mobile app can extract BMS logs, but it is a very slow and error-prone process compared to MBB log extraction.

The front of the board has a diagnostic port for a live debugging connection.

A cable to access the serial connection of the diagnostic port is described [here](http://electricmotorcycleforum.com/boards/index.php?topic=7561.0)

#### [BMS Architecture](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/Architecture)

Some general speculation here about how the BMS is designed and arranged, correlated with BMS board examination.

![2016 BMS with potting](../images/BMS_with_potting_large.png) *2016 BMS with potting*

**[TI PL536](http://www.ti.com/product/BQ76PL536)**

*Stackable Cell Monitor With Overvoltage Protector and Balancing*

The product identifier "PL536" occurs in BMS logs, referring to a TI BMS chip that handles 3-6 cells in series.

The Zero BMS has 5 of these (visible on the front of the board above).

The 5 chips divide up the 28 cell series into groups that each chip monitors (seemingly 6 per chip until the last chip handles 4 for a total of 28).

**References**

[BMS tutorial](http://www.intersil.com/content/dam/Intersil/whitepapers/battery-management/battery-management-system-tutorial.pdf)

[BMS on wikipedia](https://en.wikipedia.org/wiki/Battery_management_system)

#### [BMS Reset](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS_Reset_Procedure)

For a number of errors, the [official manual](Official_Owners_Manual.md "Official Owners Manual") recommends resetting the [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS).

![BMS indicator lights and reset windows on a 2016 DSR](../images/BMSwindows.jpg) *BMS indicator lights and reset windows on a 2016 DSR*

**Steps**

1. Key the bike off and unplug it from charging.

   Wait for the contactor to click open.
2. Uncover the battery LED indicators.

   **2015-2016:** Remove the upper rubber pad from the front of the battery case.

   **2013-2014,2017+:** Remove the rubber pad from the front of the battery case.

   The uncovered hole reveals a string of small LEDs: one red on the left followed by four green.

   They'll indicate charge level when the bike is keyed off.
3. Uncover the diagnostic connection port and reset buttons.

   **2015-2016:** Remove lower rubber pad from the front of the battery case.

   **2013-2014,2017+:** These were uncovered in the previous step.

   Notice a white plastic port coated in dielectric grease.

   Above that port are two small micro-switch buttons which are the reset buttons.
   - The *left* (as you face it) button performs a *hardware* reset.
   - The *right* (as you face it) button performs a *software* reset.
4. Press to reset

   **2013-2014:** There is only one reset button above the plastic port which performs a *hardware* reset.

   **2015+:** Take a pen (say) and depress the (right) *software* reset button for a few seconds and then release.

   Expect the BMS indicating LEDs to go dark while the button is depressed and then turn on again when release.

   The lights should stabilize after an initial startup sequence for a few seconds.
5. Check whether the error code is clear by keying on the vehicle or whatever is appropriate.
6. **2015+:** If the error is still present after a software reset, try the *hardware* reset button in the same way.
7. **2015+:** If the error is still present after a hardware reset, try both at the same time.
8. Replace the removed pads.

#### [Cell Balancing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/Cell_Balancing)

[Cell Balancing](https://en.wikipedia.org/wiki/Battery_balancing) is a self-maintenance process by the [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS).

It ensures that cells operate at very well-matched states of charge to ensure even load and better battery performance and overall lifetime.

**Mechanism**

The [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) has connections to the battery cells via the interconnect wiring and can sense cell voltage.

There are 28 contacts on the side of the back of the board (as viewed from the front of the bike looking at the battery) which connect to each cell in the "brick" series.

The BMS feeds small amounts of current to cells that are abnormally low in order to maintain battery longevity and minimize the possibility of cell damage.

It detects voltage levels on all cells, through interconnects between bricks that harness each cell in the same position in the brick's series, and through this same path able to balance cells by targeting current to the cells with the lowest voltages.

Cell balancing because of the limitations of this circuit can take a long time and is part of why Zero recommends keeping the motorcycle plugged in when unattended by default.

Stations that shut off when current draw is low (such as ChargePoint) may not allow balancing to complete.

Cell balance may be monitored with the Zero app, however only a single number is presented, the value (in millivolts) of the worst imbalance.

**Schedule**

Cell balancing often happens at low current levels, mainly during charge tapering when the charger is operating at the voltage limit in "constant voltage" mode.

It also can happen when the bike is long-term plugged in but turned off. The BMS may wake up and control charging specifically to balance the cells.

#### [Precharge](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/Precharge)

[Precharge](https://en.wikipedia.org/wiki/Pre-charge) is a [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) pre-ride startup function to charge the main power bus before closing the contactor.

The BMS has a precharge circuit for ensuring that the [contactors](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) can close without causing damaging current spikes to the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) or other components.

Precharge is necessary because of capacitors in the controller; connecting sets of capacitors electrically requires care to match voltages because of the rate at which capacitors will charge and discharge to each other to balance potentials.

See [Precharge Theory](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Precharge_Theory) for a detailed explanation.

**Operation**

- When the motorcycle is keyed on, precharge supplies a low amount of power (fused at 10A) to the controller-side main bus.
- Voltage should climb above 85V within 4-5 seconds of powering on.
- At this point, the BMS measures the voltage on both sides and decides to close the contactors.
- If this process fails, precharge will stop and then the voltage level will decay.

  You will likely see error code 25 for a precharge error on the dash (when error codes are selected for display).

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | The precharge circuit is not isolated from the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) or [accessory charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port), and can be damaged if a large transient current is induced from an outside source to a de-energized motorcycle. |

**Precharge Failure**

A recent (mid-2016) firmware update improves the robustness of the precharge logic especially when used with accessory charging systems that are permanently connected to the vehicle.

If while starting the bike, the sequence completes before the contactor closes, the green run light for the motorcycle will flash until the contactor does close.

To address a failed precharge on startup:

1. Key the bike off if after several seconds, the contactor has not shut with an audible click and the green run light is still flashing.
2. Wait 2 seconds (ensuring the dash indicator goes fully dark) and then key the bike on again.

   This should allow precharge to get a boost from residual charge from the last precharge startup cycle.
3. Repeat a few times if necessary. If the contactor never shuts, check the logs and any error codes.

### [State of Charge](https://web.archive.org/web/2025/https://zeromanual.com/wiki/State_of_Charge)

[State of Charge](https://en.wikipedia.org/wiki/State_of_charge) is a calculation meant to help estimate remaining energy in the [Battery](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery).

**Concepts**

SoC is a porportional representation; a percentage (fraction), so it is only applicable with a **known total** or max.

Riders all have experienced different ranges under different temperatures, various environmental conditions etc.

So *full* is really a subjective term, like asking *When is a balloon full? Before it pops? But if you fill it with cold air then move to a warm environment, it pops*.

- Paraphrase of [ElectricZen's explanation](http://electricmotorcycleforum.com/boards/index.php?topic=8052.msg68226#msg68226)

SoC is most easily calibrated using the battery pack's voltage at rest or near rest.

**[Battery Voltage](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery_Voltage)**

This is a rough guide to correlating *at rest* battery voltage to the state of charge.

There is respectable unofficial guidance that this curve varies as the pack ages over its lifetime.

These figures are determined from some selection of owners with logs, with minimal experimental controls.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Your mileage may literally vary! |

![% SoC vs Voltage](../images/Soc_vs_voltage.png) *% SoC vs Voltage*

![Voltage vs % SoC](../images/Voltage_vs_soc.png) *Voltage vs % SoC*

| VPack | VCell | SoC |
| --- | --- | --- |
| 115.9…116.2 | 4.14…4.15 | 100 |
| 113.9…114.24 | 4.07…4.08 | 95 |
| 112.0…112.3 | 4.00…4.01 | 90 |
| 109.76…110.8 | 3.92…3.96 | 85 |
| 108.36 | 3.87 | 80 |
| 106.96 | 3.82 | 75 |
| 105.56 | 3.77 | 70 |
| 104.16 | 3.72 | 65 |
| 103.04 | 3.68 | 60 |
| 101.92 | 3.64 | 55 |
| 101.36 | 3.62 | 50 |
| 100.80 | 3.60 | 45 |
| 99.68 | 3.56 | 40 |
| 99.12 | 3.54 | 35 |
| 98.56 | 3.52 | 30 |
| 98.00 | 3.5 | 25 |
| 97.16 | 3.47 | 20 |
| 96.60 | 3.45 | 15 |
| 96.04 | 3.43 | 10 |
| 95.76 | 3.42 | 5 |
| 95.20 | 3.4 | 0 |

**(Obsolete) SoC Indications [per protomech](http://electricmotorcycleforum.com/boards/index.php?topic=5527.msg40219#msg40219)**

Before Zero removed pack capacity readout from the [mobile app](Official_Mobile_Application.md#Statistics_Mode "Official Mobile Application"), there were some corroborating indications available:

- The app appeared to simply show kWh using Zero's max capacity rating, i.e. present voltage times present amp hours.
- The voltage and amp-hours were likely to be correct, but the kWh readout was a rough guide at best.
- The percentage reading adjusted to the estimated pack maximum over time, so as the pack aged, the reported Ah and kWh readout would decrease, but not the maximum percentage.

**Variance across Battery Pack Years**

- The sensor equipment measuring current and temperature for the battery pack improve over the years, impacting SoC indication.

  2017 model year bikes appear to have an increased range of current sensor calibration quality, improving that year's estimations.
- Cell behavior also varies over the years, generally improving in robustness.

  One can find multiple complaints of going into limp-home mode at 5-15% from 2014 SR owners, for example.

**Variance by riding conditions**

- Cell discharge is an electrochemical process that depends on the cells' physical conditions.
- The resistance of the cell (which should be low) increases with environmental factors like temperature.

  This results in reduced performance, since the resistance lowers the terminal voltage of the cells and the overall battery pack.
- At low SoC values, SoC might drop considerably once the BMS observes low terminal voltage as an indirect result of low temperatures or a cell imbalance.

  The lowest-performing cell becomes the limiting factor in pack performance at low voltage / SoC, and Zero does not provide indications to help you anticipate or diagnose this.

**Other References**

[Inaccurate SoC Estimate](http://electricmotorcycleforum.com/boards/index.php?topic=7283)

[How OEMs calculate Battery Capacity, and why it's not totally their fault they are wrong by Brandon Nozaki Miller](https://www.electric.motorcycles/post/how-oems-calculate-battery-capacity-and-why-it-s-not-totally-their-fault-they-are-wrong)

#### [BMS SoC Estimation](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/SoC_Estimation)

**[BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) [State of Charge (SoC)](https://en.wikipedia.org/wiki/State_of_charge) Estimation**

SoC is inherently an abstract / simulated measure, not one that can be directly proven with enough physical inputs.

The actual proof of state of charge is to fully discharge the battery, running an integral of current as discharged (this is the Current Method of Estimation).

But a "full" discharge must be decided from a measurement, too, taking minimum cell voltage, which sometimes (and possibly for certain cell generations) can have a single cell fall in voltage early causing SoC to drop early.

And this voltage can be a dynamic result of the rate of discharge, so that restarting the bike after a few minutes' rest period can show a higher SoC than before.

**[BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) estimation modes**

1. [Current Integration Method](https://en.wikipedia.org/wiki/State_of_charge#Current_integration_method), or "coulomb counting", which measures the battery current over time and estimates its integral or sum.

   Battery current will reverse for regen mode and for charging, and this is measured and included in the estimation.
2. [Voltage Method](https://en.wikipedia.org/wiki/State_of_charge#Voltage_method), a fairly inaccurate but simpler method where battery voltage is measured and then dynamically compensating the voltage reading by a correction term proportional to the battery current, and by using a look-up table of battery's open circuit voltage vs. temperature.

   Voltage correlates to SoC well at the empty and full states, but less well in the plateau area of 20-80%.

**Method Switching**

The SoC method may switch during operation, and should be indicated in the event logs.

It appears to change primarily when charging starts or stops; it is probably triggered by the battery's Charge Mode state.

When the method switches, SoC may change dramatically (by 12% or more) with no clear explanation.

**Temperature Effects**

Batteries are chemical systems that can be very complicated to summarize.

One of the main capacity factors is the pack temperature, which is determined by both outside temperature and any heat produced internally from resistance during charging and discharging.

Temperature appears to be a significant factor in building the SoC estimation for either method.

**Examples**

Walk through the logic of SoC boundary parameters with some stock Zero equipment.

**Equipment**

[Farasis 25Ah cells](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Cells) (using the datasheet available) in a 28 cell series.

**Static Voltage Walkthrough**

The 116V reported by the mobile application at 100% SoC corresponds to 4.14V (=116V/28).

0% state of charge at least naively then would correspond to 92.4V ( = 3.3V × 28).

The nominal cell voltage listed (3.65V) then corresponds to a nominal pack voltage of 102.2V, which does reflect the relatively stable battery voltage reading near the middle of the state of charge cycle in steady state.

**Reframing (per Terry)**

Zero will let you discharge to about 88 volts and up to 116.4 volts.

By the Farasis data sheet, this is using the full capacity of the cells with the exception of about 4 volts from the whole pack.

84 volts would be 3.0V per cell but 88 volts is pretty close.

88 volts is about 3.14V per cell and there is less than 1% energy left at 3.14V.

In any case, the state of charge calculation is driven by attempting to bracket vehicle usage to stay in this range.

The desired voltage range (to maintain battery chemistry over the stated lifetime) drives stated limits, coupled with an estimation of the amp-hours remaining from any given point in the collective state of the battery pack.

#### [SoC Calibration](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/SoC_Calibration)

**SoC Drift**

The SoC has an inherent *drift* based on inherent sources of error:

- An integral is not generally computable from time-sampled measurements.
- Battery current sensors seem to have calibration targeted at the high end of the range (highway speeds) and do not have a known recalibration program; likely a non-linear output.
- Temperature measurements must rely on sensors in specific positions in the battery (with no feasible ideal position).

Steady throttle usage should experience less drift than wildly varying usage, but the inherent measurement problems still lead to some drift.

**SoC Drift Correction**

SoC drift is only really eliminated by the battery reaching an equilibrium state.

The BMS seems to recalibrate SoC for the 100% condition:

- Pack voltage at 116.2V.
- Battery state at rest via *either*:
  1. 0A charge or discharge current.

     with some few minutes time spent with the charger disconnected.
  2. ~0.8kW charge rate

     **NOTE:** observed by testing with a controllable switching supply; onboard charging can substitute.

### [Battery Storage and Capacity with Age](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Storage_and_Capacity_with_Age)

Chemically, the cells mainly age in two ways:

1. The electrolyte reacting with the active components of the cathode and anode in the cells, and releasing gas (calendar life).
2. The interaction between the lithium ions and the anode/cathode blend that causes a small amount of damage each time they are cycled. (Cycle life)

You just have to come to terms with the fact that from the moment the battery pack is manufactured it will very slowly lose overall capacity regardless of whether you use it or not. Li-ion batteries are good at holding their charge so you don't need to worry about letting them stand for a long time, providing they've got a reasonably good state of charge (SoC). At 40-50% SoC the overall capacity loss due to aging is minimized. At full charge the aging effects are increased but not by such a great amount that it should cause any great concern. For some owners it might be wiser to follow Zero's recommendations and just leave the bike plugged in for however long you plan to store the bike. This at least makes sure the individual cells stay balanced with each other and there's little risk of them dropping to a very low SoC at which point the aging effects begin to increase. If you let the SoC drop below their minimum threshold you run the risk of the battery pack becoming unusable. I think that's why Zero recommend leaving the bike plugged in over winter. If there's some sort of power cut mid-winter and the bike isn't checked for a few months, then at least there's a good chance the battery won't have discharged too much.

Farasis recommendations:

> The manufacturer might state that you will get 500 cycles from a battery and they will be referring to full cycles. However, if you only ever use 10% of the capacity from a full charge and then top it up, you will get more cycles from it before the battery health drops to 80%. In this example you are likely to get 1500 cycles from a battery that you only ever discharge to half it's capacity. That's assuming that all other variables remain the same. In day-to-day use, variations in state of charge and temperature are more likely to affect battery life than how you cycle the battery. Taking Zero's claim's of an estimated battery pack life of 496,000 km using city ranges it would take at least 2,250 full cycles to achieve this (2014 Zero S 11.4 kWh). Taking into account the loss of capacity in this period and the figure is bound to be more like 2,500 cycles. Most trips and daily commutes will probably drop the battery to 40-50% SoC thus increasing the number of cycles we would get from the battery. Let's say we average 60 miles between charges of a 100 mile combined range over the life of the bike. Then let's allow ourselves 3,000 cycles before the battery drops to 80% health. That's still 180,000 miles. Even if we then halve that to allow for temperature and aging (very unlikely even in harsh conditions) we get a very, very conservative estimate of 90,000 miles. That should give even a heavy commuter a good five or six years of use before noticing significant reduction in range. Even then, a daily average of 60 miles would still give you a 20 mile reserve.

If you do decide to leave it at 40-50% SoC you also need to be organized enough to check the bike every couple of weeks or so. It wouldn't hurt to charge it up after a few months, leave it plugged in for a few days to make sure the cells get properly balanced, then take it for a ride to bring the SoC down to the 40-50% level again before leaving it for the next few weeks or months.

I have no doubt that the good people at Zero have done their sums, know the specifications of the batteries in detail and are confident that their battery packs will have at least 80% health after five years even if the bike is never ridden and left plugged in all the time. Zero also state in their specifications that their battery packs are good for hundreds of thousands of miles before they reach 80% of their original stated capacity. That in itself should be enough to put your mind at rest, but if it isn't then perhaps these golden rules should help:

1. Don't leave the bike standing empty for more than a few days.
2. If you have to store the bike for a long time, then either leave it plugged in and don't worry about it, or leave it at 40-50% SoC but keep an eye on it.
3. Just use your bike as much as you can and don't worry about the battery. The engineers have thought all this through and are backing it up with a five year warranty. The whole scene will be different in five years time, so it isn't worth thinking about.

### [Battery Temperature Effects](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Temperature_Effects)

**Performance**

Battery internal resistance is higher at lower temperatures, which means that while riding, losses to battery internal resistance mean a loss of range at lower temperatures.

Farasis quotes internal cell resistance as <2mΩ but it's not exactly clear how this translates into calculating those losses without some description of how that trends over temperature and charge rate.

The warmer the battery is, the lower these losses will be.

Below freezing temperatures, the battery chemistry will not allow effective charging at all, and Zero provides protections to prevent this until the battery's temperature has been raised sufficiently.

It follows that to get maximum performance, charging and discharging repeatedly at a high rate will raise cell temperature enough to reduce internal resistance so more will be delivered to the motor.

**Degradation at high temperatures**

Temperature is a bigger factor than state of charge when it comes to aging. Apparently, for every increase of 10F degrees in battery temperature across its lifetime, battery deterioration over that lifetime can double.

**Heat Production**

It is worth noting though that Li-ion batteries shouldn't generate a lot of heat when charging at normal rates.

On a Zero, charging at or below 4kW will not produce much heat.

Therefore, even if you live in a hot climate and have just been on a ride, the cells should cool down overall even while they are charging (although direct sunlight on the battery will add more heat).

You might want to be a little more careful if fast charging in a hot climate but don't forget that the BMS will either reduce the charge rate or stop charging altogether if the cell temperature exceeds the limits that the engineers have set. They have set these limits on the conservative side to avoid any claims on that five year warranty.

**Storage**

If you are going to store the bike, it makes sense to store it somewhere cool.

Fridge temperature is probably best but never store below freezing.

If you don't have the option of storing it somewhere cool, then don't worry about it.

### [Battery Memory Effects](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Memory_Effects)

There are *no memory effects* with Li-ion chemistry.

Some 'Smart' battery management systems might recommend performing a deep discharge followed by a full charge from time to time.

This helps re-calibrate the system and give better estimations of capacity remaining.

However, there is *no need to do this* from purely a cell maintenance point of view.

All Li-ion batteries have protection circuits (Zero uses the [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) and [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Contactor)) to keep the cells within their safe operating voltage range.

You can therefore simply charge and discharge at will and not worry about charging a battery that is half full.

### [Rate of Charging and Discharging](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Rate_of_Charging_and_Discharging)

The Farasis cells have a nominal capacity of 25 Ah (as of 2013-2014).

Each cell has a maximum continuous discharge rate of 100 A (4[C rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate)).

You would have to discharge the battery in 15 minutes to achieve that, which is impossible to achieve normally.

Conveniently, the Zero S 11.4 should achieve a range of approximately 70 miles at a constant speed of 70 mph.

That would result in a full discharge in an hour.

Even maintaining 80 mph, the maximum sustained speed of the bike, it's difficult to empty the battery pack in less than half an hour.

So the cells are operating well within their specifications.

The maximum charge rate for Zero battery packs is 25A for each cell or brick (2013-2014), which would mean a full charge in an hour, referred to as a 1[C rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate).

Even with a 6.6kW level 2 charge, you're only going to get a full charge in 2 hours, probably more like 2.5 hrs as the charge rate will drop as the battery reaches capacity.

Yet again, the cells are under relatively little stress even with a fast charge.

### Protections

#### [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor)

The main [contactor](https://en.wikipedia.org/wiki/Contactor) is a high-capacity relay-operated switch separating the battery's positive side from the bike's propulsion systems.

It mutually protects the battery and the bike's systems from damaging each other, particularly for rush currents or overcurrent conditions.

**Model**

Contactors for the 2013+ years are [GIGAVAC GX-series contactors](http://www.gigavac.com/catalog/power-products/gx-series).

The 2013 year contactor is not identified, and some reported an occasional failure mode where "contactor welded shut" could occur.

2014+ years feature the [GX11](http://www.gigavac.com/products/gx11), which appears to fail safe open by design (SPST-NO) and has had no significant reported issues.

**Location**

The 2013+ power pack contactor is housed within the "dog house", an enclosed area extending from the main power pack enclosure top face at the rear.

For the [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Zero_Aftermarket) accessory and bricks and long bricks, each enclosure has one contactor operated by the BMS within.

**Behavior**

See [Charging Control Unit](#Charging_Control_Unit) and [Contactor Limits](#Contactor_Limits).

**Theory ([ref](http://electricmotorcycleforum.com/boards/index.php?topic=7040))**

A contactor is a large relay: it allows a fairly small voltage/current signal to switch a much larger voltage/current.

It has two sides:

1. The drive/coil side (control).
2. The load (contact) side.

On the drive/coil side, there's a "kickback" diode which handles the inductive spike caused when the drive to the coil ceases.

Without that diode, the energy represented in the magnetic field inside of the coil would have no place to go, so it would cause a voltage spike which can be damaging to components.

The kickback diode gives that energy somewhere to go, allowing it to ramp down fairly slowly without a big voltage spike.

Depending on how the coil side of the contactor is wound, it has a certain current requirement to pull the contactor shut, say 12V @ 100mA, which will be provided by the driving circuitry.

There's not necessarily any relationship between the *coil rating* and *contact rating*, except that bigger (higher-current rated) contacts might be heavier and require higher coil current to get the armature to move.

The kickback diode only needs to carry this amount of current, regardless of the contact side current.

If a 3A kickback diode is specified for that contactor, it will be adequate for any contact side current.

The *make/break* current is the rating for the contact side of the contactor.

You won't actually want to make or break the contactor under the limiting conditions (you'll always want to both make and break the contactor at exactly 0 amps), but in an emergency, it's rated to do so without the contacts welding together -- and an emergency is what the contactor is there for.

In automotive use, you often see the coil set up for 12V, drawing maybe 100mA (the current can vary widely though).

That small current pulls the contacts together, which switches on the high-current side.

##### Contactor Limits

Zero's effective contactor limit for the charging rate is 95% of 1[C rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate).

The BMS will open the contactor for the following conditions:

**Inactivity**

If the motorcycle is keyed off and not otherwise set in charging mode, the contactors will open after a few seconds.

If the motorcycle is keyed on and not otherwise set in charging mode, and then 30 minutes pass without control input.

Twisting the throttle is sufficient to reset this timer; otherwise restart charging once it happens.

**Voltage**

Voltage is too low or too high outside its safe operating range.

If voltage is too high (117V):

1. Confirm with the Zero mobile application
2. Attempt to bring it back to normal range by discharging the battery:
   - operating the motor (fastest but requires a closed contactor, and the Sevcon won't operate above 118V) or:
   - turning on all available electrical loads.

If voltage is too low, charge by any means necessary:

Prefer the onboard charger or an equivalent rate source through the charging port.

In an emergency, the regen feature can be used to charge the battery through the motor.

Drive the motor by spinning the rear axle with a suitable power source, with the bike in Custom Mode with regen set to 100%.

**Power**

Incoming power exceeds 1[C rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate) continuously for a minute. A 1[C rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate) charges the battery fully in 1 hour.

For a battery with 13 kWh max capacity, this value will be 11.4 kWh nominal / 102V = 110A (say).

If the charge rate is too high for the battery, downgrade the charge rate manually and restart.

Field testing indicates that the short time setting for the contactor opening is 30 seconds, and that a 20 second period under that limit will reset it.

This may vary due to environmental conditions like ambient temperature.

**[Temperature](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery_Temperature_Limits)**

If the battery temperature (not ambient) is outside safe operating bounds:

|  | Cold Battery |  | Normal | Hot Battery |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Range | operation prevented | charging prevented |  | charging tapered | operation prevented | damage likely |
| (F) | … -22F | -22F … 32F | 32F … 110F | 110F … 122F | 122F … 140F | 140F … |
| (C) | … -30C | -30C … 0C | 0C … 43C | 43C … 50C | 50C … 60C | 60C … |

The Zero battery will emit heat while its charging rate exceeds 4 kW, and it will cool if under that threshold.

If temperature is out of safe range, do whatever is appropriate to bring the temperature back in range.

**Calculating Contactor Limit Per Bike**

Per Zero's specs pages:

Maximum capacity (kWh) = COUNT(cells) × (cell capacity rating (Ah)) × MAX(cell rating (V))

**Example**

A 2015 SR w/ Power Tank has 15.3kWh max, 13.5 kWh nominal, with a 102V nominal voltage, so is nominally rated at 133 Ah.

1C rate means that it can charge at up to 133A.

At 10% actual SOC (3.4 volts per cell), 1C = 3.4 volts per cell × 28 cells in series × 133 A = 12.7 kW.

At 95% SOC (4.1 volts per cell), 1C = 4.1 volts per cell × 28 cells in series × 133 A = 15.3 kW.

These are DC power ratings; AC input power will read 10 to 20% higher (due to conversion losses).

**Contactor Limit Per [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Zero_Aftermarket) or module**

The current capacity will be proportional to the number of bricks vs 4 providing a scaling factor.

Or, more directly, the Ah rating on the label indicates the 1C rate.

|  |  |  | Capacity (kWh) |  | Voltage |  | Capacity | Contactor Limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Year | Cell | # Bricks | Max | Nominal | Max | Nominal | (Ah or 1C amps) | A (95% assumed) |
| 2013 | 25Ah | 4 | 11.4 | 10.0 | 116.4 | 102 | 98 | 93 |
| 2014 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| 2015 | 27Ah | 4 | 12.5 | 11.0 | 〃 | 〃 | 108 | 103 |
| 2016 | 29Ah | 4 | 13.0 | 11.4 | 〃 | 〃 | 112 | 107 |
| 2017 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 | 〃 |
| 2018 | 32Ah | 4 | 14.4 | 12.6 | 〃 | 〃 | 125? | 119? |

#### [Battery Fuse](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Internal_Fuse)

Each [brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Brick) has an internal 300A fuse for protection in case the contactor welds shut.

The contactor welding shut is very difficult if not impossible by design in post-2013 models.

Naturally, if this fuse blows, your battery warranty may be in question, and certainly if you open the pack to replace it.

### [Battery Stress Factors](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Stress_Factors)

The following factors speed up degradation:

**Hot Temperatures**

This causes the electrolyte to become more reactive. Farasis claims to have one of the most stable electrolyte blends in the business, and use a lot of proprietary tech to keep the cathode/anode blend as least reactive as possible, but the effect is unavoidable.

**High Voltage**

Again, The higher the potential between the cathode and anode, the faster the reaction between the electrolyte and the actives occurs.

**Very Low Voltage**

Below a certain voltage (2.0-2.2V/cell) the potential between the cathode and anode is such that the battery has used all its high potential lithium, and so it starts picking on the next easiest thing, which is the copper.

This process is super ugly, as it electroplates the copper off the negative foils (anode) and electrodeposits it onto the positive foils (cathode). PERMANENT IRREVERSIBLE DAMAGE. This is super dangerous too, as the next time it is charged, that copper gets blasted back to the negative foils and lands wherever it feels like, as the anode isn't designed to deal with copper Ions. So they form big crystal sharp structures called dendrites, which at best can pierce the separator and cause high self discharge and gassing as the electrolyte nucleates (gas builds up, the cell goes to 0V and looks like a balloon) , or at worst, the dendrite is able to get a solid connection between the cathode and anode, and this causes the cell to short internally and results in fire.

Luckily for you, Zero has an amazing BMS and pack topology that sips hardly any power from the cells in a key-off state, but you still can murder the bike by approaching 0% SOC as slowly as possible until it is at its absolute lowest SOC (state of charge) and the BMS shuts the bike off. What happens is that the bike has the smallest amount of reserve battery then, and the BMS sipping away at that small amount will eventually murder the cells over a period of several years.

### [Battery Longevity](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Longevity)

If Zero are putting a five year warranty on their battery packs, it's quite possible that they believe they will last ten years.

Tesla are saying that their battery packs are good for 15 years apparently.

It seems a lot like buying a normal bike or a car.

Feel confident that it will give you at least five years or 50,000 miles of good service.

If you don't mind buying a five year old vehicle and taking a bit more risk, then you should achieve double.

Time will tell and sellers will be able to quote actual range figures to prospective buyers.

**References**

[Just How Far Can You Push an Electric Car Battery?](https://jalopnik.com/just-how-far-can-you-push-an-electric-car-battery-1827929360), part of Jalopnik's Formula-E coverage

[What can 6,000 electric vehicles tell us about EV battery health?](https://www.geotab.com/blog/ev-battery-health/)==References and further reading==

- [Why do lithium batteries die? (video)](https://www.youtube.com/watch?v=pxP0Cu00sZs)

### [Battery Future](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Progress)

**Rate Of Improvement**

Battery technology is improving every year, but not at the same rate as computer technology.

A 10% per year increase in capacity might be a reasonable expectation.

We can always hope that there will be a significant breakthrough that makes is way to production and changes the state of the art much quicker.

For the time being though, we have robust technology that should give you five to ten years of service and a range of about 100 miles of mixed riding as long as you don't spend much time on fast roads.

**What To Expect For Now**

It's perfect for many city commuters and people who like relaxed rides taking the country roads.

You will need an ICE bike for longer journeys and touring, unless you are willing to plan in long charging stops.

If you can use your bike for your commute or have regular trips that cover less than 100 miles a day, then range anxiety won't be an issue.

### [Battery Best Practices](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Best_Practices)

Basically, the way to kill a Zero battery the fastest is to either:

- Ride it to absolutely dead as possible, and then store it in a shed for six years, or
- Store it at absolutely tip top charge in direct sunlight in a super hot desert in Arizona somewhere.

Either way, you will still struggle to kill them before the 5-year warrantee is up.

So, to prolong your battery life, you can do the exact opposite:

- Store the bike in a *cool* place with a *stable* temperature at a *medium SoC*.
- About 60% or so is fine for S/DS (one BMS sipping on 3-5 cellboxes) or 70% for the FX modules (one BMS per cellbox).

Definitely consult [Zero's own official charging recommendations](https://www.zeromotorcycles.com/owner-resources/charging-recommendations/) as well.

When you get done riding your S/DS hard on a hot day, let it cool down for 4-6hrs before charging it.

This takes less time for FX modules.

**Fast Charging**

Fast charging is fine, but know that around the **.8C** mark is the point where at normal ambient temp, you go from cooling off to heating up.

If your pack is already hot from a ride through the desert at WOT, and you fast charge, you are still going to be on a hot pack when you continue your WOT journey.

This is not a big deal, but it's helpful to bring the battery temperature back down to minimize the aging effects that this accumulates over time.

The BMS will keep you from really breaking your pack, so don't worry about it.

### [Battery Construction](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Construction)

Z-Force Power Pack construction is a heavily armored box case.

Dimensions for the full [Monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Monolith) are 10" width, roughly 17" height and 14" depth.

The [Long Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Long_Brick) enclosure for 2017+ models is the same at roughly half the depth, and of course the storage area on S/DS models with this Power Pack has about the same dimensions minus clearances and dividing bracket allowances.

### Battery Removal

#### [Power Pack Module Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Power_Pack_Module_Removal)

Removing a [Power Pack Module](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module) from an [XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform) model.

The OEM manual covers this, and it's a primary feature of the XMX platform that the power packs can be swapped or removed.

As of 2017, XMX platform models (FX/FXS/FXP) are assembled by default with a [Long Brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Long_Brick) 6.5kWh pack that cannot be easily swapped or removed; it is bolted into the frame.

The option to buy a model with individual power pack modules is still available for an additional cost.

#### [Monolith Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Monolith_Removal)

Removing the [Monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) from an [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) model:

This is very involved, only suitable for a dealer or experienced electrical engineer equipped with a hoist, because the frame must be lifted vertically off of the battery, and the battery must be electrically detached from the systems safely.

There is also almost no realistic reason to do this for a battery under warrantee.

**Steps**

- These are a rough sketch of the process.

1. Remove the belly pan and onboard charger.
2. Disconnect all cables leading to the battery.
3. Disconnect the grounding strap to the Y-shaped underseat frame piece.
4. Place the motorcycle on a center lift that can balance the battery on its own.
5. Harness the frame into a hoist and put some of the load onto that hoist.

   The hoist should be rated to lift the bike's weight entirely.
6. (Possibly) remove the front wheel and/or forks.
7. (Possibly) remove the rear wheel and/or swingarm.
8. Use an allen key wrench to remove the 2 bolts on each side of the lower battery mount (4 total).
9. Lift the frame.

### [Battery Pack Rebuild](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery/Pack_Rebuild)

This is the most unrecommendable thing to do for a Zero owner who is not an experienced electrical engineer.

The battery warranty will be completely forfeit, its watertightness will be compromised, and there is likely little a non-expert can do to improve the design.

And you could be killed.

**Official Replacement Support**

For older Zeros whose battery warrantee has expired, contact a dealer or Zero's corporate technical support line to see what they can support.

Zero has in the past offered reasonable trade-in value for older motorcycles which are difficult to support and rare.

Pack upgrades have been performed years after a model is released, under the battery warranty, when the pack is proven to be defective.

It remains to be seen whether a recycling trade-in will be offered.

**See Also**

- [Battery rebuilds for Gen1 batteries](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen1/Battery_Rebuild)

## [Charging](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging)

The [CCU](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Control_Unit) (Meanwell-charger-equipped models only for 2013 and 2014FX) and [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) manage the [onboard charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) and the battery's [contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) to prevent or cut off charging in a number of conditions.

**Operation**

The [contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) makes [an audible “click” sound](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Contactor_Click_Sound) when closing and opening.

- Don't twist the throttle after turning the bike on until you hear that click.

  The bike prevents itself from lurching forward if the contactor closes while the throttle is open, but you shouldn't rely on that or find yourself surprised.
- Similarly, do not start charging without a closed contactor.

  The [onboard charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) will enable charging mode by CAN bus communications, or keying the bike on can at least close the contactor for drive mode.

  Charging mode can be retained through [charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) inputs at the signal pins, but they cannot initiate charging mode.

### [Charging Indications](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Indications)

Indications of charging activity:

**External**

The [dash](#Instrument_Cluster) charging light will **flash** while charging.

The [dash](#Instrument_Cluster) charging light will be **solid** once fully charged.

The BMS front indicator window shows 4 LEDs.

The number of LEDs lit indicates the SOC level in quarters.

**Voltage (verifiable with the mobile app)**

Battery voltage will rise with its state of charge while charging from below 20% and then stays relatively constant (easing from 100V to 104V) from 20% to 80% where it starts rising again.

A Zero battery will have a full charge when it has 116V while at rest.

During a charging session, the voltage will dynamically increase by as much as 1V so expect 117V at the end of a full charge until charging stops.

Indications for the Zero battery state of charge while charging may have a significant inaccuracy at high charge rates.

Typically, indicated SoC will lag (lower than) actual SoC towards the upper end of the range (80% - 100%).

Turning the motorcycle off and letting the contactor open and waiting for several seconds should restore charge accuracy.

The BMS historically would thereby reset its method of SoC estimation to a static voltage-based method.

The battery will charge most efficiently between roughly 20% and 80% state of charge, with voltage high enough that current limits allow more power input.

At higher voltages, chargers taper out of concern to maintain battery condition.

### [Charging Heat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Charging_Heat)

The Zero battery will emit heat above a charging level of 0.4[C](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate) (4kW for a 4-brick pack), and will naturally cool below that threshold.

Expect several degrees Fahrenheit rise when performing a full charge near a 1[C rate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/C-Rate).

The cause is best characterized as [wikipedia:Internal resistance](https://en.wikipedia.org/wiki/Internal_resistance) of the battery, driven by current flow.

The power wasted from this characteristic will be *roughly* proportional to the square of the current flowing into the battery.

**External Inputs**

On the [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform), the [Onboard Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) is contacts the bottom face of the battery case and will conduct some heat into the battery as it operates.

**Discharge Heat**

Discharging a battery at a very high rate can also produce heat.

The internal resistance from charging seems to be higher *for a given current* than the internal resistance from driving/discharge.

**High Temperature Guidance**

See the [hot weather usage](Usage.md#Hot_Weather "Usage") recommendations for thorough guidance.

If the battery temperature is already high enough to cause concern about the next charging phase, ride at relatively modest speeds to allow ventilation to cool it faster than discharge heats it up.

Use a battery temperature indication to help understand this.

### [On-board Charging Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Inlet)

The onboard [charger](#Charger) is connected to an IEC C14 inlet hard-mounted to the lower left side of the frame above the footpeg.

**Fasteners**

The C14 inlet is fastened to the inside of the frame by 2 tiny M2×7.5 socket head bolts taking a 2.5mm Allen/hex key.

The bolts are positioned above and below the body of the inlet; the lower can be accessed from the front, and the upper from the rear.

The space around the fasteners is very tight, facing the motor, and difficult to see or access.

**NOTE:** Because of the close proximity to the motor, front sprocket, and other electrical connections, take care not to drop or lose these bolts as you remove them.

**Rubber Plug**

A rubber plug is included to protect the inlet from the elements (which then protects the onboard charger from sparking currents that can degrade it over time).

Keep the rubber plug on when the inlet is not connected to a cord.

![MY2016DSR onboardchargerconnector dustcap.jpg](../images/MY2016DSR_onboardchargerconnector_dustcap.jpg)

**Plug Replacement**

1. Remove the left pillion footpeg bracket

   ![MY2016DSR onboardchargerconnector fasteners.jpg](../images/MY2016DSR_onboardchargerconnector_fasteners.jpg)![MY2016DSR onboardchargerconnector pillionbracketwrench.jpg](../images/MY2016DSR_onboardchargerconnector_pillionbracketwrench.jpg)
2. Remove the fasteners holding the electrical receptacle

   ![MY2016DSR onboardchargerconnector pillionbracketremoved.jpg](../images/MY2016DSR_onboardchargerconnector_pillionbracketremoved.jpg)![MY2016DSR onboardchargerconnector connectorremoval.jpg](../images/MY2016DSR_onboardchargerconnector_connectorremoval.jpg)
3. You now have access to remove/replace the rubber protective plug

   ![MY2016DSR onboardchargerconnector dustcapremoval.jpg](../images/MY2016DSR_onboardchargerconnector_dustcapremoval.jpg)

### [Accessory Charging Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port)

The [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) platform includes a [charging circuit](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Circuit) terminated by a hard-mounted brown [Anderson SBS-75X connector](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Anderson_connector) to support OEM and third-party additional chargers.

**Input**

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Only supply DC power to this port in the battery's normal range, or **risk catastrophic damage to the battery**. |

All external chargers are switching power supplies that turn AC (or sometimes DC!) power at a wider range of voltages into DC that behaves well with Zero's battery technology and voltage range.

2012 Zero batteries operate in a lower voltage range than 2013+ Zero batteries; chargers for one range of years should never be used on another range of years.

**To use**

- Remove the rubber boot cover and plug in the charger(s).

  ![MY2016DSR accessorychargingport stockfromfactory.jpg](../images/MY2016DSR_accessorychargingport_stockfromfactory.jpg)![MY2016DSR accessorychargingport cutzipties.jpg](../images/MY2016DSR_accessorychargingport_cutzipties.jpg)![MY2016DSR accessorychargingport removezipties.jpg](../images/MY2016DSR_accessorychargingport_removezipties.jpg)![MY2016DSR accessorychargingport connectchargeplug.jpg](../images/MY2016DSR_accessorychargingport_connectchargeplug.jpg)![MY2016DSR accessorychargingport reseatrubbercover.jpg](../images/MY2016DSR_accessorychargingport_reseatrubbercover.jpg)

  As delivered, the rubber boot cover will be secured with zip ties. Remove them first.

  2013 models do not include the rubber boot; it is a good idea to install one to protect the plug over time, though.
- Use the onboard charger in conjunction with the accessory charging port to keep the motorcycle in charging mode (allows keying off while charging among other things).
- Replace the rubber boot after unplugging the charger(s).

| Platform | Years | Location |
| --- | --- | --- |
| X | 2013+ | Forward of the motor on the right lower side of the frame, under a plastic panel with 5 fasteners. |
| S | 2011-2012 | Right side of the battery. |
| 〃 | 2013 | Above the motor on the right side (opposite the ODB-II port). |
| 〃 | 2014+ | Above the motor on the left side (more accessible than 2013), covered by a rubber boot. |

**Location**

![DSR Charging Port from above the motor](../images/Dsr-above-motor.jpg)![DSR Charging Port from under the tail](../images/Dsr-under-tail.jpg)

**Mounting (SDS Platform)**

One or two small H2.5 Allen key socket head bolts run up through the connector's holes into a collared insert on a flanged edge of the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate).

**Detaching (SDS Platform)**

1. [Remove the left lower plastic panel](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Lower_Plastics_Removal) first for access.
2. Either:
   - Use a very low overhead / right-angle H2.5 Allen key wrench from the left side of the bike ahead of the vertical frame stanchion.
   - [Pull the board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate_Removal) up by enough room to fit a right-angle Allen key underneath, between the connector and the motor fins, about an inch or two.

**Enable Line**

The Anderson SBS-75X connector has two signaling pins which the [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) employs in conjunction with a feature of the [Zero Quick Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Zero_Quick_Charger) to indicate charger presence.

The feature is not completely understood, but it operates this way:

- When the contactor is shut, if the enable line detects charger presence, the contactor will remain shut until or unless the enable signal is removed, or a safety limit is detected by the [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) requiring opening the contactor.
- The enable line has no effect if the contactor is open.

Implementing the feature has been performed in various ways.

- See [the XMX off-bike charging article](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Charging_Off-Bike) for enable pin wire-up or [charging Y-cable fabrication](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Fabricate_Charger_Y-Cable) for how to combine enable signals safely.
- One minimal implementation joins the two pins in a simple 100kΩ resistive circuit.

  Full pack voltage would supply 1mA current to such a circuit at most, so a high-current wire is not needed; just a solid circuit pinned appropriately for the connector with an inline resistor and weather+abrasion+strain-proofing).

  | | |
  | --- | --- |
  | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | This implementation has not been officially vetted by Zero, and there may be unknown effects operating with such a circuit long-term |

**Removing the rubber boot**

Only for when you are replacing the Anderson connector permanently with another type/shape of connector.

The rubber boot is held by a nylon "fir tree" plug.

![Nylon "fir tree" rivet](../images/Example.jpg)

Use a flat tool (screwdriver, nylon pry tool, etc) to wiggle between it and the mounting plate until loose.

After removing, you can install the rubber boot elsewhere using (for example) an M5 bolt and some washers.

![Anderson rubber boot](../images/Anderson_removal.jpg)

### [Charging Circuit Fuse](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Circuit_Fuse)

The [charging circuit](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Circuit) has a fuse encapsulated in a cable that protects the battery from charging at too high a rate.

**Affected Circuits**

- **2013:** the charging fuse acts on the [accessory charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port), and does not disable the [onboard charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger).
- **2014+:** the fuse acts on the circuit containing both the [accessory charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) and the [onboard charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) but has a much higher limit.

**Location**

On the right side of the bike under the seat behind the battery, near or under quite a few 12V cable runs.

![JJN-100 Fuse.jpg](../images/JJN-100_Fuse.jpg)

| Platform | Years | Current Limit (Continuous) | Power Limit (Continuous) | Product |
| --- | --- | --- | --- | --- |
| X | 2013+ |  |  |  |
| S | 2013 | 30A | 3kW | [Eaton JJN-30](http://www.mouser.com/ProductDetail/Bussmann-Eaton/JJN-30/?qs=bpnLQM2ZShxX0X37lSZxFw%3D%3D) |
| 〃 | 2014+ | 100A rated, 85A slow limit | 10kW | [Eaton JJN-100](http://www.mouser.com/ProductDetail/Bussmann-Eaton/JJN-100/?qs=vco6xy%252beH1pHxfCrJKaBAA%3D%3D) |

**NOTE**

2013 Battery Pack Longevity [Recalls](Recalls.md "Recalls")

The battery pack replacements performed by the manufacturer due to discovered defects wind up being upgrades to 2015 and then 2016 model year power packs, and seem to include upgraded [charging circuits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Circuit), so those older models will have the higher-rated fuse and work like the newer bikes, charging-wise.

**Replacement**

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | This fuse is not meant to be user-serviceable, and could be very dangerous to replace without the exact same specification. |

The fuse is downstream from the [contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor), so if the contactor is open (it should be if you can't charge and the bike is keyed off), it should be de-energized.

Verify this with proper testing equipment.

It's a huge inline fuse within adhesive heat shrink, so it's difficult to extract and replace.

The wires do have ring terminals once you get the fuse out, so you could wire in a fuse breaker. Or if in a pinch just bolt them together.

**Fuse Part Investigations**

A 2014 SR was found to have an [Eaton JJN-100 fuse](http://www.mouser.com/ProductDetail/Bussmann-Eaton/JJN-100/?qs=vco6xy%252beH1pHxfCrJKaBAA%3D%3D), a fast-acting fuse rated for 300V and 100A.

[Datasheet for the Eaton JJN-100](http://www.mouser.com/ds/2/87/Bus_Ele_DS_1025_JJN-347438.pdf)

If the 2014 match is correct, a [JJN-30](http://www.mouser.com/ProductDetail/Bussmann-Eaton/JJN-30/?qs=bpnLQM2ZShxX0X37lSZxFw%3D%3D) would seem to be the match for a 2013 Zero (same datasheet as above).

There was supposition of a 60A limit on 2014 motorcycles, implying a TTN-60, but that has not been proven with evidence.

## Electrical System

### Lights and Signals

#### Headlamp

Zero's models ship with halogen bulbs.

##### [X Platform Headlamp](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Headlamp)

**Pre-2014**

Hella circular reflector unit (possibly [the Vision Plus 5¾" conversion headlamp](http://www.myhellalights.com/index.php/products/auxiliary-lamps/sealed-beam-conversion-headlamps/vision-plus-5-75in-conversion-headlamp/)).

**2014+**

In 2014, the FX acquired a dual projector configuration with a W3W stock running light.

![X headlamp front.jpeg](../images/X_headlamp_front.jpeg) ![X headlamp markings 1.jpeg](../images/X_headlamp_markings_1.jpeg) ![X headlamp markings 2.jpeg](../images/X_headlamp_markings_2.jpeg)

**Adjusting angle (2014+)**

There are two retaining bolts on each side of the headlamp assembly.

Loosen all four bolts, pivot the assembly to the angle as desired, and then re-tighten to fix it in position.

##### [S Platform Headlamp](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Headlamp)

![2013+ LSL Urban Headlight](../images/Lsl-urban-headlight.png) *2013+ LSL Urban Headlight*

![2013+ LSL Urban Headlight (rear)](../images/Lsl-urban-headlight-rear.png) *2013+ LSL Urban Headlight (rear)*

**Pre-2012**

Hella circular reflector unit (possibly [the Vision Plus 5¾" conversion headlamp](http://www.myhellalights.com/index.php/products/auxiliary-lamps/sealed-beam-conversion-headlamps/vision-plus-5-75in-conversion-headlamp/)).

**2012+**

For 2012+ models, the Zero's stock headlamp assembly is the [LSL Urban Headlight](https://spieglerusa.com/lights-indicators/headlights-by-lsl/urban-headlight-kits/lsl-headlight-chrome-3290.htm) with an H4 bulb in a 9003 / HB2 socket, and a W3W stock running light.

LSL Urban headlight housing dimensions: 190mm width, 260mm height, 125mm depth.

The headlamp housing OEM is by TRIOM with part number T7869010. It can be bought on the Italian market (ebay.it or amazon.it or such) for $100 instead of $160 in the US.

**Power**

The stock headlamp draws about 55/60W which is the largest regular 12V electrical load by default.

The electrical load doesn't impact range much (110Wh over 2 hours compared to 11+kWh yields 1% range difference), *unless* you ride a very slow long travel leg for, say, offroading.

However, it does heat up the housing glass.

**Bulb Retainer**

The headlight is fastened in by a plastic bracket that locks when rotated, and covered with a rubber boot to protect from moisture.

**[[../Headlamp Removal|Removal]]**

**Tools**

- 3mm (H3) Allen key
- 4mm (H4) Allen key

**Steps**

1. Unbolt the two lower mount screws with a 4mm Allen key.
2. Unbolt the two upper mount screws with a 3mm Allen key.
3. Disconnect the headlight and running light wires to detach the assembly completely.

**[[../Headlamp Bulb Replacement|Bulb Replacement]]**

**Video guide**

- [Zero SR - How to swap a headlight bulb](https://www.youtube.com/watch?v=iHgjR7gBV_U):

**Steps**

1. **Suggestion:** [Unbolt the headlamp assembly](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Headlamp_Removal) (with 3mm and 4mm allen wrenches) from the metal brackets to get enough room to work.

   ...unless you have very small hands and move the existing cabling out of the way.
2. Detach the existing bulb's cable at the plug.
3. Pull the rubber cover away from the headlamp.
4. Twist the retaining bracket to release the bulb.

   **NOTE:** Avoid touching the bulb; oil and dirt from your fingers can cause the bulb's surface to heat up while operating and could age the bulb prematurely. Keep the bulb clean.
5. Place the retaining bracket and rubber cover around the new bulb and press and rotate to fix it in place.

**NOTE:** For a 2013-2014 model, the plastic retaining bracket might require some filing to fit another bulb with its assembly to hold it in and lock properly. Later models have an easier shape to fit.

**Calibration**

When replacing the headlamp, check the light pattern emitted and adjust the set screw in the headlamp housing to get a suitable projection angle.

**[[../Running Light Replacement|Running Lamp Replacement]]**

This replaces the W3W running light bulb on the [[../Headlamp|SDS Platform Headlamp]].

**Steps**

1. [[../Headlamp Removal|Remove the headlamp]]
2. Turn and/or wiggle the rubbery boot at the rear of the running light to extract it from the headlamp assembly.

   Optionally, unplug the running light wiring connector first, if it makes it easier to manipulate.
3. Remove the bulb and insert its replacement.

   As with any bulb, take care not to leave skin oil or other residue on the bulb's surface, which could thermally stress it over time.
4. Re-insert the running light by its rubbery boot into the headlamp assembly.
5. Re-connect the running light wiring connector if appropriate.
6. Re-install the headlamp.

**Adjusting angle (2013+)**

There is a set screw on the upper-right rear face of the headlamp housing to adjust the angle of illumination.

Adjust this while the bike is sitting fully upright.

Remove the lower screws and swing the headlamp on the two upper bolts to access the screw while adjusting.

Turn the set screw clockwise to aim the headlamp down, counterclockwise to aim it up.

#### [Turn Signals](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Turn_Signals)

Zero uses a triangle-shaped turn signal housing on a flexible stalk.

The turn signals are oriented so the front and rear are interchangeable if you swap sides going from front to rear and vice versa.

| | | |
| --- | --- | --- |
| ![Left-hand front (right-hand rear) turn signal](../images/ZM65-03462.png) *Left-hand front (right-hand rear) turn signal* | ![Right-hand front (left-hand rear) turn signal](../images/ZM65-03463.png) *Right-hand front (left-hand rear) turn signal* | ![Turn signal drawing](../images/ZM65-03463-drawing.png) *Turn signal drawing* |

**Maintenance**

Always check for functioning turn signals (running light, headlamp, turn signals, brakes).

**Connectors**

Threaded insert into the headlamp and tail bracketing (not identified, could be M8) with a notch to hold their position.

Barrel-style single wire Molex connectors (2 per signal):

- [1 Pin Molex .062 Female Plug Connector w/Pins 03-06-1011](https://www.molex.com/molex/products/datasheet.jsp?part=active/0003061011_CRIMP_HOUSINGS.xml)
- [1 Pin Molex .062 Male Plug Connector w/Pins 03-06-2011](https://www.molex.com/molex/products/datasheet.jsp?part=active/0003062011_CRIMP_HOUSINGS.xml)

**Turn Signal Bulbs**

**2013+ (Gen2, Gen3?)**

Type PY10W, similar to 1156, but the side pins are offset by 150 degrees rather than 180.

Also called BAU15S or R10W.

The glass is amber (as the lenses are clear) and smaller, since the regular 1156 glass is too big.

AF1 Racing references [#AP8127489](http://www.af1racing.com/store/Scripts/prodView.asp?idProduct=5890) as "amber turn signal bulb, staggered pins"

**2009-2012 (Gen1)**

Clear 1156 incandescent bulbs, very standard.

#### [Turn Signal Flasher](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Turn_Signal_Flasher)

The turn signal ("blinker") flasher is a simple three prong flasher relay.

It's attached directly by a plug so is easily replaced if it fails (or for an LED compatible unit).

**Label**

```
Flasher Unit 12V
2x10W
PN: 8078
Made by Ecie Cheng Du
```

*or*

```
GUILERA
Flasher Unit 12V
10+10W+1,2W
P.N. 013341
```

**Low Noise Revision**

As of 2016, the part is [revised with the description "low noise"](http://www.af1racing.com/store/Scripts/prodView.asp?idProduct=89625).

This suggests reduced electronic and/or audible noise.

This model of flasher relay is noticeably quieter, and that year coincides with reports from Zero management of EU EMF/EMC noise compliance expenditures.

**Silent Revision**

As of 2020?, the part is from the manufacturer Guilera and makes no audible noise.

This again suggests reduced electronic noise, again likely as a result of EU EMF/EMC noise compliance expenditures.

**Wiring**

The orientation is specific. Reversing the (+) and (-) wiring may be necessary if you buy the wrong orientation of relay.

Look at the pins with the middle **L** (center)(Load) pin on top and the **B** and **E** below it to each side.

- **2018+:** The orientation should be **E (-)** (left), **L** (center/top), then **B (+)** (right).

  Ref. [report from a 2019S owner](https://www.electricmotorcycleforum.com/boards/index.php?topic=9780)

  This orientation is know as a **CF14** relay [per pacificcricket](http://electricmotorcycleforum.com/boards/index.php?topic=8751.0)
- **2013-2017:**

  The orientation should be **B (+)** (left), **L** (center/top), then **E (-)** (right)

  This orientation is know as a **CF13** relay

| Years | Platform | Location | Photo |
| --- | --- | --- | --- |
| 2012 | S/X | Under the seat below the fuse block. | ![2012S-obdii-port-and-fuse-block.jpg](../images/2012S-obdii-port-and-fuse-block.jpg) |
| 2013+ | X | Behind the right fairing | ![2013-fx-flasher-relay.jpg](../images/2013-fx-flasher-relay.jpg) |
| 〃 | S | In front of the front plastics area under the frame "wishbone" with other electrical connections. | ![Tank-relay-connectors.jpg](../images/Tank-relay-connectors.jpg) |

#### [Tail Light](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Tail_Light)

The tail light enclosure includes the rear running and brake lights.

The lights inside are LEDs.

The assembly is made by [TRIOM](http://www.varrocgroup.com/triom_lighting), an Italian company.

![Tail Light (rear)](../images/Brake_light_rear.png) *Tail Light (rear)*

![Tail Light (front)](../images/Brake_light_front.png) *Tail Light (front)*

![Tail Light (top)](../images/Brake_light_top.png) *Tail Light (top)*

The product made for Zero has not been identified so far, but has shown no failures, either.

#### [Horn](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Horn)

The horn is a [K70-H Electromagnetic Disc Horn](http://www.leb.it/eng/k70_electromagnetic_disc_horn.html), P/N 45-06774 for model years 2014-2020.

| | |
| --- | --- |
| Current | 1.5A @ 13V |
| Sound Level | 109dB @ 2m |
| Pitch | 430Hz |
| Weight | 155g |

### Switchgear

#### [Fuse Block](https://web.archive.org/web/2025/https://zeromanual.com/wiki/12V_Fuse_Block)

The 12V fuse block protects the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) from faults in all the 12V components on [Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2) models.

[Gen3](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3) models have a fuse block but the protection has redundant upstream components in the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB), so the fuse block just helps with isolation.

| Platforms | Years | Components | Rating | Notes | Photo |
| --- | --- | --- | --- | --- | --- |
| S,X | 2013+ | Accessory circuit | 10A | Sumimoto plug (all years) and SAE plug (2014+ years) | ![2013 Fuse Block](../images/2013_S-DS_Fuse_Block.jpg) *2013 Fuse Block* |
| 〃 | 〃 | Headlamp | 10A |  | 〃 |
| 〃 | 〃 | Instrument cluster (Dash) <br> running lights | 5A |  | 〃 |
| 〃 | 〃 | Turn signals (Flashers) <br> horn <br> brake lights | 10A |  | 〃 |
| 〃 | 〃 | Ignition key | 5A |  | 〃 |
| 〃 | 2015+ | ABS circuit and the ignition key | 5A |  | ![2015-2016 Fuse block (label inaccurate; rotated 180°)](../images/Fuse-block-2016.jpg) *2015-2016 Fuse block (label inaccurate; rotated 180°)* |
| 〃 | 〃 | ABS pump | 25A | limited duty | 〃 |
| 〃 | 〃 | ABS valve | 10A |  | 〃 |

**Wiring**

The fuse block connects to the positive side of the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) output on its left side.

The downstream wires enter a mesh sleeve, through a ferrite ring to clean up RF interference, and lead forward into a larger sleeve that runs (for the S-Platform) along the left side of the forward tank area.

**Location ([SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform))**

Under the seat under the [Y-shaped frame join piece](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Subframe)'s left rear leg.

For 2015+ models, the 25A ABS pump fuse is mounted to the back of the block and may require removing the frame join piece to access fully.

**Location ([XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform))**

On the frame under the right side front body panel.

For 2015+ models, the 25A ABS pump fuse is mounted to the frame above the block.

**Location ([FST Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FST_Platform))**

Under the rider's seat on the right side.

#### [Ignition Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Switch)

The Ignition switch is a locked turn-key operation for enabling the bike with a reasonable amount of physical security.

The switch is operated by the [Ignition Lock](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Lock).

**Location**

Through the center of the upper tripleclamp, ahead of the steering stem and handlebars and below the dash.

**Routing**

The ignition wiring runs under the steering head to the MBB. This implies that the MBB is at least partially powered while the bike is keyed off.

**Security**

Position the steering in the locked position to prevent easy access to the wiring which facilitates theft/override via "hotwiring".

**Connections**

MBB pins (per 2013 trace)

- 4 - Orange/White 20AWG
- 5 - Orange/Black 20AWG

#### Handlebar Switch Housing

The handlebar switch housing assemblies seem generic but have Torx T22 security bolt fasteners making inspection and maintenance more difficult than average.

#### [Kill Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kill_Switch)

The kill switch (or engine cutoff/cutout switch) is a toggle switch on the right handlebar switch assembly prevents motor operation as a separate control from other interlocks.

**Mounting**

On the right handlebar switch assembly.

**Operation**

Push up/forward to cutoff motor operation.

Push down to enable motor operation.

**When to Cutoff Motor Operation**

- Whenever the bike should not be operating.

  This is a redundant safety mechanism to prevent injury or damage.
- If the vehicle is on its side after a crash or other incident.

  This prevents spinning up the wheel.
- Whenever someone unfamiliar with the motorcycle is sitting on it or nearby.

  If they intentionally or unintentionally touch the throttle, this prevents their lack of familiarity from causing a surprise excursion.

**Troubleshooting**

The [status](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) command in the MBB console can report its reading.

While energized, a voltmeter will indicate 5V across the input leads if the switch is open, and 0V if shut.

While de-energized (and confirmed), resistance across the switch will be high if open, and low if shut.

**Connections ([Gen2](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2))**

It is wired as a digital input to the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB).

SPST where the off position is an open circuit, for failsafe considerations.

Red 20AWG - (assumed high/positive-5V) to MBB pin 23 (per 2013 trace)

White 20AWG - (assumed low/0V) to MBB pin 24 (per 2013 trace)

#### [Kickstand Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Switch)

The [Kickstand](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand) has a safety cutout switch (really a sensor) to prevent motor operation while at rest.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | **Kickstand Sensor Electrical Equipment Hazard** <br> The connector is three pronged and needs to be connected correctly or can damage the MBB irreparably. <br> **Do not disconnect or reconnect** while the vehicle is keyed on or contactor is shut to be safe. <br> **Do not short any wires together to bypass.** <br> This is a Hall effect sensor usually containing or using sensitive measurement IC's and therefore not a simple switch. |

**Part**

From observation, the [Asahi Denso](https://en.ad-asahidenso.co.jp/products/motorcycles/) CE122 proximity sensor appears to be the part match, also used on some Triumph and KTM motorcycle models.

From the 2016 SR's sensor to its connector, the wires are Blue, Pinkish Red, and Black.

While the bike is keyed on and contactor is closed, Blue measures a stable 5V, Red measures ~2.7V and varies (need to scope this), and black appears to be a signal ground/input (needs verification when I'm not tired).

Some KTM riders with the Asahi Denso CE122 sensor have reported success using commercial bypass kits.

- [Reportedly](http://electricmotorcycleforum.com/boards/index.php?topic=9276.msg81168#msg81168), a [KTM sidestand switch bypass kit](https://slavensracing.com/shop/sidestand-switch-bypass-removal-kit-ktm-690-950-990/) can work on a Zero without issues.

  [Instructional video](https://www.youtube.com/watch?v=tglAUxsl51M)

One such user suggested these are merely a potted 2.2kOhm resistor between the Red and Black wires (link here).

Zero motorcycles can be far more sensitive to faults on signalling pins so this should not be attempted unless you absolutely know what you are doing, and are willing to risk having to replace your MBB.

talonreaper has had luck on a 2016 SR with a 2.7kOhm resistor between the red and black kickstand sensor's wires to get home from being stranded in an emergency.

This is still not advised.

North or South pole magnetism activation? TODO

**Connector**

The connector appears to be a Sumimoto MT sealed series connector MT-3S-2, p/n 6180-3241.

Ref. [Corsa Technic reference page for 6180-3241](https://www.corsa-technic.com/item.php?item_id=232&category_id=126&manufacturer_id=44)

This connector appears to be a very standard application for Japanese motorcycle interlock sensors for sidestands/kickstands.

**Troubleshooting**

Raise the kickstand for testing only with the rear wheel lifted off the ground via a [stand or lift](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Lift).

The [status](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) command in the MBB console can report its reading.

**Maintenance**

An unconfirmed suggestion per this [Side stand safety switch](https://www.electricmotorcycleforum.com/boards/index.php?topic=9824) discussion on EMF:

Since I was worried about the condition of my side stand safety switch and never having looked at it before, I got on my hands and knees under the bike and checked it out.

I noticed that there were a couple of wires that went into a plastic sheath that protects the wires and their connections within the switch housing from damage.

But I also noticed that the sheath's opening faces forward and it seemed like water and muck could be forced into the opening and perhaps short out the switch contacts under extreme conditions.

So what I did was to squirt some silicone sealant into the opening and sealed it off.

Hopefully, that will eliminate any possibility of water getting into the switch when riding on wet streets.

**Bypass**

*If there is a compelling justification worth risking warranty damage*, the sensor interlock preventing operating the powertrain may be bypassed.

The bypass should be performed via [MBB settings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) configuration.

| Pin # | Wire Color | Wire Gauge |
| --- | --- | --- |
| 10 | Yellow/Black | 20AWG |
| 11 | Orange/Black | 20AWG |
| 27 | Red | 20AWG |

**Removal**

See [Kickstand Switch Removal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Switch_Removal)

**Replacement**

See [Kickstand Switch Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Switch_Replacement)

#### [Tail Wiring](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tail_Wiring)

Tail wiring includes the [tail lights](#Tail_Light) (running and braking power), each rear [turn signal](#Turn_Signals), and the license plate illuminator.

| Photo | Connector | Function | Wire Color |
| --- | --- | --- | --- |
| ![ZeroTail17b.jpg](../images/ZeroTail17b.jpg) | Standard Suzuki or Honda brake light (3-wire) | Tail light power | Brown |
| 〃 | 〃 | Brake light power | White with red stripe |
| 〃 | 〃 | Negative/Return | Black |
| 〃 | Single pin connector <br> Socket: [Molex 03-09-2011](http://www.molex.com/molex/products/datasheet.jsp?part=active/0003092011_CRIMP_HOUSINGS.xml) [[15]](http://www.mouser.com/ProductDetail/Molex/03-09-2011/) [[16]](https://www.digikey.com/product-detail/en/molex-connector-corporation/03-09-2011/WM1303-ND/) <br> Pin: [Molex 03-09-1011](http://www.molex.com/molex/products/datasheet.jsp?part=active/0003091011_CRIMP_HOUSINGS.xml) [[17]](http://www.mouser.com/ProductDetail/Molex/03-09-1011/) | Left turn signal power | Green |
| 〃 | 〃 | Negative/Return | Black |
| 〃 | 〃 | Right turn signal power | Grey |
| 〃 | 〃 | Negative/Return | Black |

**Note about Braking Regen**

Braking regen is activated by the pressure switch on the front brake lever or hydraulic switch on the rear brake pedal, through the rear brake power circuit.

If that circuit doesn't complete (due to a failed bulb or wiring disconnect), braking regen seems to not activate.

**Routing**

Tail wiring runs through a sleeve by the [controller](#Controller) on the left side.

Ensure it is protected from chafing by the controller cover.

Turn signal wires run through a pair of holes where the tail stalk meets the subassembly underneath the tail.

### Schematic

#### [S-Platform Schematic](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Schematic)

Burton has been maintaining this Zero wiring diagram based on his now-highly-modified 2013 Zero S.

It is schematically correct for that year but could use improvement relating the physical routing and there are missing details like the precharge circuit.

**Routing**

- [Power Cable Routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Power_Cable_Routing)
- [12V Electrical Routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Electrical_Routing)

**Diagrams**

[Diagram by Burton for 2013S](http://electricmotorcycleforum.com/boards/index.php?topic=3603)

![2013S wiring diagram preview](../images/ZeroWireDrawing_2013_S_11-4_R-1-3-0_no-grid_highRes-scaled.png) *2013S wiring diagram preview*

**Latest versions**

[1.3.0 Gridded PDF](../images/ZeroWireDrawing_2013_S_11-4_R-1-3-0_grid_highRes.pdf "File:ZeroWireDrawing 2013 S 11-4 R-1-3-0 grid highRes.pdf")

[1.3.0 No Grid PDF](../images/ZeroWireDrawing_2013_S_11-4_R-1-3-0_no-grid_highRes.pdf "File:ZeroWireDrawing 2013 S 11-4 R-1-3-0 no-grid highRes.pdf")

**2015+ Notes**

the 12V fuse block has more slots for ABS, at least, and the cabling layout is denser.

#### [X-Platform Schematic](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Schematic)

See the [XMX electrical routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Electrical_Routing) article for the layout of these wires and cables.

| | |
| --- | --- |
| **Latest version** <br> [1.1 PDF](../images/2016_FX_Wiring_1-1.pdf "File:2016 FX Wiring 1-1.pdf") | [![2016 FX wiring diagram hyperlinked](../images/2016_FX_Wiring_1-1-preview.png)](https://web.archive.org/web/2025/https://zeromanual.com/wiki/2016_X-Platform_Wiring_Diagram) |

[Keith's thread with updates](http://electricmotorcycleforum.com/boards/index.php?topic=7547.0)

| | |
| --- | --- |
| ![preview](../images/Anderson_pins.png) | ![preview](../images/Anderson_pins_wire_side.png) |

**Earlier Model Years**

[Zero DS 2011 wiring diagram](http://electricmotorcycleforum.com/boards/index.php?topic=7373.msg63470#msg63470) forum thread with a 2011/2012 XU diagram

### [OBD-II Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/OBD-II_Port)

Zero models all have an [OBD-II](https://en.wikipedia.org/wiki/On-board_diagnostics#OBD-II) port that is reasonably accessible for troubleshooting, diagnostics, and data collection.

Its wiring is non-standard; to connect, we offer the following references:

- [How to build a cable to access the MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/How_to_build_a_cable_to_access_the_MBB) for how to build a cable to work with it.
- [The aftermarket section on OBD-II solutions](Aftermarket.md#OBD-II_Diagnostics "Aftermarket").

#### [OBD-II Port Location](https://web.archive.org/web/2025/https://zeromanual.com/wiki/OBD-II_Port_Location)

| Platform | Years | Photo |  |
| --- | --- | --- | --- |
| [S](https://web.archive.org/web/2025/https://zeromanual.com/wiki/S_Platform) | 2011-2012 | In the tank area facing the forward frame join where the [fuse block](https://web.archive.org/web/2025/https://zeromanual.com/wiki/12V_Fuse_Block) sits. | ![2012S-obdii-port-and-fuse-block.jpg](../images/2012S-obdii-port-and-fuse-block.jpg) |
| [SDS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) | 2013 | Above and behind the motor next to the [accessory charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Accessory_Charging_Port), on the left-hand side. | *difficult to photograph* |
| 〃 | 2014-2015 | Above and behind the motor next to the [accessory charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Accessory_Charging_Port), on the right-hand side. | *difficult to photograph* |
| 〃 | 2016+ | Under the seat on the left side just behind frame bulkhead that the tank plastics rest on for 2016 models. | ![OBD-II location for 2016](../images/Obd-ii-2016.jpg) |
| [XMX](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform) | 2011+ | Under the left side tank plastics. | ![OBD-II location for FX](../images/Obd-ii-fx.jpeg) |
| [FST](https://web.archive.org/web/2025/https://zeromanual.com/wiki/FST_Platform) | 2020+ | Inside the tank storage compartment |  |

### Routing

#### S Platform Routing

##### [S Platform Power Cable Routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Power_Cable_Routing)

Power cabling transmits full traction power from the [battery](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery) to the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) and then to the [motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor).

The cables are very thick, armored, and are covered in an orange mesh wrap for abrasion resistance and to indicate the danger involved if the cables are damaged.

**Battery to Controller**

- B+ (positive) and B- (negative) cabling runs in the power harness from the back of the monolith or long brick pack to the B+ and B- terminals on the motor controller.

  The position of the routing from the back of the battery varies by pack geometry:
  - 3- or 4-brick monoliths will have a doghouse on top but the main power coupling will be lower on the rear face.
  - Longbrick packs reside in the forward half of the monolith area of the frame with the doghouse on top. The power coupling seems to run along that top face of the compartment.

  The cables enter the central area of the frame and rise forward of the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate) to emerge in front of the controller and run rear towards the lugs.
- [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank) cabling runs from the doghouse on that [brick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brick) to the same B+ and B- terminals on the motor controller.

  The cabling needs to route under the frame arch that supports the [tank plastics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Tank_Plastics) and [seat](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Seat), typically under the right corner.

  The cabling then extends back under the [Y-shaped subframe piece](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Subframe) to the controller terminals.

  Power tank cabling lugs should be stacked above the main pack's lugs on the motor controller terminals.

**Controller to Motor**

M1, M2, and M3 phase cabling runs from the corresponding terminals on the motor controller.

The cables run forward from the phase terminals, below the [Y-shaped subframe piece](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Subframe) and then down the right inside of the vertical frame stanchion to the motor, behind the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate).

The cables are really affixed to the motor, so it's more accurate to say they run up from the motor through this area of the frame and then emerge and run back to the controller.

##### [Charging Cable Routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Charging_Cable_Routing)

The charging cables transmit power from the [Onboard Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) and the [accessory charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) to the main power packs via the main bus.

**Routing**

- [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform)

  On 2014+ models with Calex chargers, the [Onboard Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) DC output cable runs along the right side of the rear face of the [Monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) compartment, where it joins via Anderson SB50(?) brown connector to the charging circuit to the main pack.

  The [accessory charging port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) cable runs forward from the underside of the [board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate) up through the [charging circuit fuse](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Charging_Circuit_Fuse) to the main pack.

  Since the main pack may be a 3 or 4-brick [Monolith](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Monolith) or a [Longbrick](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Longbrick), the routing varies in how it reaches either the doghouse or the back plane of the battery.
- [XMX Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform)

  See [the XMX electrical routing article](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Electrical_Routing) to see the layout of these cables.

##### [S Platform 12V Routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Electrical_Routing)

This describes routing for the 12V electrical system on [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform) models.

For power cable routing, see the [Power Cable Routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Power_Cable_Routing) article.

**Under The Seat**

The 12V [fuse block](https://web.archive.org/web/2025/https://zeromanual.com/wiki/12V_Fuse_Block) is bolted under the [Y-shaped frame bracket](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Y-Shaped_Underseat_Subframe) under the seat.

The underside terminals lead to the positive terminals from the [DC-DC converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) below on its left side.

(The following picture has one flaw: the fuse label is rotated 180°; layout is reverse of the label)

![Fuse block](../images/Fuse-block-2016.jpg)

The terminals on top enter a mesh sleeve, through a ferrite ring to clean up RF interference, and lead forward into a larger sleeve that runs along the left side of the forward tank area.

The 12V accessory port cable is lower gauge than the others and has a crimped connection that splits into two circuits for 2014+ models.

The positive side crimped connection is just two inches from the fuse block under the first sleeve, wrapped in vinyl self-adhesive tape.

**Video Guide**

- [Quick and dirty Youtube guide to this areaa](https://www.youtube.com/watch?v=yig2RtRuIoY):

**Tank Area Left-Side Routing**

All cabling leading to the steering controls and instrument cluster runs along the left side of the frame tank area wrapped in a bundle.

The largest connector on the left side leads to the instrument cluster. There is a smaller 4-pin connector there for ABS circuits (probably).

![2013 Tank Electrical Layout](../images/2013-tank-electrical-layout.jpg)![2015+ Tank Electrical Layout](../images/Tank-electrical-layout.jpg)

**Negative/Return**

The negative side connection for all of the forward 12V circuits is halfway along the tank area under a longer stretch of vinyl self-adhesive tape.

The merged output leads back down to the DC converter between the forward seat and the motor.

**Tank Area Front Mounting**

A group of components are clamped to the underside of the front part of the frame in front of the tank:

![Connectors and relay under front frame](../images/Tank-relay-connectors.jpg)

- The turn signal flasher relay.
- 12V accessory ports: Sumimoto connector and the SAE connector (2014+).
- The 3-pin headlamp connector.

**Tail Routing**

Towards the tail, one sleeved bundle runs past the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) on the left side and handles:

- Turn signals
- Brake and running lights.
- License plate illuminator.

The turn signal wires run through a pair of holes where the tail stalk meets the subassembly underneath the tail.

#### [X Platform Routing](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Electrical_Routing)

![2016 FX Electrical Locations](../images/Electrical_locations.png)

**Overview**

The 12V fuse block is located behind the right hand front body panel.

The turn signal flasher relay is also under the right panel.

The SAE connector is located under the bundle of wires on the right side front body panel.

In the following photo, the cable is on top, but it can be routed around.

It only has power when the motorcycle is keyed on.

![Zero FX wiring](../images/Zero-fx-wiring.jpeg)

**High Voltage Fusing**

![HV Fuses Left Side](../images/Electrical_HV_fuse_locations_Left_side.png) ![HV Fuses Right Side](../images/Electrical_HV_fuse_locations_Right_side.png)

## Troubleshooting

### [Dash Display](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster/Troubleshooting)

How to use the [instrument cluster](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster) to extract basic diagnostics from the bike, and also understand when and how it's malfunctioning.

**Entire Display Flashes**

If the dash display in its entirety is flashing after keying the bike on, this indicates an onboard charger self-test failure.

Key the bike off and wait for a few seconds and retry, and it should clear.

**No Backlight**

Check your running lights and license plate lights, if those are also out then check the fusebox (see: seat removal).

If the fuse pops right away, there is a short circuit in the wiring harness (*as happened to a MY2016 DSR pinched wiring harness (or mouse nest!) to the license plate lights*).

Disconnect the tail light module and the display module connectors; if the fuse still pops, try removing the tail and tracing the short circuit.

#### [System Warning Sequences](https://web.archive.org/web/2025/https://zeromanual.com/wiki/System_Warning_Sequences)

This is a quick lookup for the red sequences flashed by the [dash](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster) System Warning Indicator (a red triangle with an exclamation mark within it).

These are derived from the [Official Owners Manual](Official_Owners_Manual.md "Official Owners Manual") only for roadside reference and owner community annotations and links.

**Overview**

The red indicator light in the lower part of the display sometimes will flash a repeating sequence.

The [Official Owners Manual](Official_Owners_Manual.md "Official Owners Manual") lists what they mean, usually related to system startup.

Often enough, keying the bike off and on is the way to re-test.

**System Warning Troubleshooting**

1. Toggle the Instrument Cluster's Display A to show [Error Codes](Error_Codes.md "Error Codes").
2. Check the corresponding [Error Codes](Error_Codes.md "Error Codes")

   Some will be expected like *kickstand down* based on your context.

   Focus on topical system errors related to the System Warning.
3. Attempt a basic reboot:
   1. **Charging:** disconnect the external power source from the vehicle.
   2. Key the bike off.
   3. Wait several seconds or a minute in length depending on severity of the error.
   4. Key the bike on, checking for a normal startup sequence, contactors closing, and no errors.
4. If the System Warning persists, *and* it is related to the BMS, perform a [BMS Reset Procedure](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS_Reset_Procedure) (soft and then hard reset).
5. If the System Warning persists, attempt to extract MBB logs.

   **Urgent/Roadside:** Email logs to yourself, then decode using [a log parser](http://home.hasslers.net/zerologparser/log_parser.php).

   **Non-Urgent or Important:** Email logs to Zero.
6. If no clear resolution is at hand, contact Zero and/or your local dealer to schedule servicing.

| # | Blinks | Description | Cause | Guidance |
| --- | --- | --- | --- | --- |
| [1](#1) | ············ | Fast constantly | Safety Override is Active |  |
| 〃 | · · · · · · · · | Fast intermittently | [BMS Isolation Fault](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Isolation_Faults) | Check the [BMS Isolation Fault](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Isolation_Faults) section of the manual <br> Moisture and/or dirt are the most likely culprits. |
| 〃 | — = 1 long <br> - Charge Indicator blinking fast constantly <br> - or all blinking dash segments |  | Charger Not Charging | Probably a CAN Error <br> Unplug the bike and wait a minute to re-engage |
| 〃 | — | 1 long | Cutout switch engaged or [Kickstand Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Switch) Disabled | Disengage the cutout switch and/or raise the kickstand. |
| [2](#2) | ·· | 2 short | Self-test failed |  |
| [3](#1-3) | ·   ··· | 1 short, then 3 short | [High Throttle Disable](Error_Codes.md#1 "Error Codes") | The throttle signal is abnormally high or disconnected. <br> See [Error Code 1](Error_Codes.md#1 "Error Codes"): Check [throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) rotation and connections. |
| [4](#1-4) | ·   ···· | 1 short, then 4 short | [Precharge Fail](Error_Codes.md#27 "Error Codes") | See [Error Code 27](Error_Codes.md#27 "Error Codes"). |
| [5](#1-5) | ·   ····· | 1 short, then 5 short | [Low Power Pack Disable](Error_Codes.md#7 "Error Codes") | See [Error Code 7](Error_Codes.md#7 "Error Codes"): Battery voltage is too low to operate <br> Charge *slowly* as soon as possible. |
| [6](#2-1) | ··   · | 2 short, then 1 short | [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) Error | See [Error Codes](Error_Codes.md "Error Codes") related to the [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor). |
| [7](#2-2) | ··   ·· | 2 short, then 2 short | [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) Error | See [Error Codes](Error_Codes.md "Error Codes") related to the [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger). |
| [8](#2-3) | ··   ··· | 2 short, then 3 short | CAN Error |  |
| [9](#2-4) | ··   ···· | 2 short, then 4 short | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) Disable | See [Error Codes](Error_Codes.md "Error Codes") related to the [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle). |
| [10](#2-5) | ··   ····· | 2 short, then 5 short | [Module Variance Too High](Error_Codes.md#32 "Error Codes") | See [Error Code 32](Error_Codes.md#32 "Error Codes") |
| [11](#3-3) | ···   ··· | 3 short, then 3 short | [Battery Temperature Sensor Fault](Error_Codes.md#18 "Error Codes") | See [Error Code 18](Error_Codes.md#18 "Error Codes"): A temperature sensor failure reduces safety; arrange a dealer visit. <br> Not *urgent* to fix unless other battery problems are apparent from logs/etc. |
| [12](#4-1) | ····   · | 4 short, then 1 short | [Contactor Welded](Error_Codes.md#26 "Error Codes") | See [Error Code 26](Error_Codes.md#26 "Error Codes") |
| [13](#4-3) | ····   ··· | 4 short, then 3 short | [Motor Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) Error | See [Error Codes](Error_Codes.md "Error Codes") related to the [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller). |
| [14](#4-4) | ····   ···· | 4 short, then 4 short | [Loopback Error](Error_Codes.md#35 "Error Codes") | See [Error Code 35](Error_Codes.md#35 "Error Codes") <br> Reconnect either an expected second battery module or Power Tank, if present. <br> Otherwise, reconnect the blanking plug. |
| [15](#5-1) | ·····   · | 5 short, then 1 short | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) Startup Error |  |
| [16](#5-2) | ·····   ·· | 5 short, then 2 short | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) Internal Disable |  |
| [17](#5-3) | ·····   ··· | 5 short, then 3 short | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) Internal Fault |  |
| [18](#5-5) | ·····   ····· | 5 short, then 5 short | Miscellaneous Error |  |

#### [Error Codes](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Error_Codes)

How to use the [2014+ instrument cluster](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster) to extract self-reported diagnostic codes from the bike.

| Code | Description (official) | Manual Section | Community Notes |
| --- | --- | --- | --- |
| [0](#0) | No Error |  | Almost abnormally normal! |
| [1](#1) | High [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) | [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) | Likely throttle connection or potentiometer issue |
| [2](#2) | [Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) Temperature Warning Stage 1 | [Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) | Near upper temperature limit; corresponds to blinking temperature light on the dash |
| [3](#3) | Motor Temperature Warning Stage 2 | [Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Z-Force_Motor) | Reached upper temperature limit; might involve cutbacks or shutdown |
| [4](#4) | [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) Temperature Warning Stage 1 | [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) | Near upper temperature limit; corresponds to blinking temperature light on the dash |
| [5](#5) | Controller Temperature Warning Stage 2 | [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) | Reached upper temperature limit; might involve cutbacks or shutdown |
| [6](#6) | BMS Throttle Enable Wire Error | [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) |  |
| [7](#7) | Low [Battery](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery) Voltage | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | Should only happen near/below 0% SoC or 84V dynamic pack voltage. <br> This can reset for a bit if the bike is powered off for a few minutes; charge ASAP. |
| [8](#8) | High Battery Temperature Status | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | Can happen during a >4kW charge or while operating at speed in a hot environment. <br> Reduce battery load! |
| [9](#9) | Low Battery Temperature Status | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | Can happen in winter storage; will prevent charging. <br> Use a space heater or bring the bike inside ASAP to prevent battery damage. |
| [10](#10) | Battery Temperature Warning Stage 1 | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) |  |
| [11](#11) | Battery Temperature Warning Stage 2 | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) |  |
| [12](#12) | Reserve Partition Warning | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) |  |
| [13](#13) | Reserve Switch Warning | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) |  |
| [14](#14) | Safety Override Active | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) |  |
| [15](#15) | [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) Attached But Not Charging | [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) |  |
| [16](#16) | CIB Contactor Compromised | [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) |  |
| [17](#17) | [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) Error | [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) |  |
| [18](#18) | [Battery](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery) Temperature Sensor Fault | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) |  |
| [19](#19) | High Charge Current | [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | The contactor limit for charging was reached and the BMS opened the contactor. <br> Key the bike off and on to reset. |
| [20](#20) | BMS Low Isolation | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) |  |
| [21](#21) | Board Vpack Error | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) |  |
| [22](#22) | Board Temperature Error | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) or [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) |  |
| [23](#23) | Post Error | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) or [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | Power-On Self Test diagnostic result |
| [24](#24) | Startup Error | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) or [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | Firmware boot diagnostic result |
| [25](#25) | Contactor Open Warning | [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | This indicates the contactor is open. <br> This may be appropriate given what safety interlocks are in play. |
| [26](#26) | Contactor Welded Error | [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | Only 2013 models have contactors that can realistically weld shut <br> The code indicates battery voltage on the power harness or bus when there shouldn't be any. |
| [27](#27) | [Precharge](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/Precharge) Error | [Precharge](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS/Precharge) | Indicates bus voltage didn't climb enough in the required time period to close the contactor safely. <br> Try keying the bike off and on again over a period of a few seconds to retry. |
| [28](#28) | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) Isolation Fault | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | Indicates any kind of ground indication as measured by various BMS circuits. |
| [29](#29) | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) Isolation Danger | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | Indicates a ground indication as measured by various BMS circuits. <br> The BMS protects itself by opening the contactor. |
| [30](#30) | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) CAN Error | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | CAN bus error to/from the BMS, as reported by the MBB? |
| [31](#31) | [SEVCON](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) CAN Error | [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) | CAN bus error to/from the Sevcon controller, as reported by the MBB? |
| [32](#32) | Module Variance Too High | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | Indicates that a module within the power pack is varying too much from its siblings (voltage? current?). <br> Provide a balancing charge with the onboard charger or any <0.4C charger. |
| [33](#33) | SEVCON Error Turn Off | [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) |  |
| [34](#34) | Charge Error Turn Off | [Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) |  |
| [35](#35) | [Loopback](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS_CANBus_Loopback) Error | [Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank) | The connector for BMS1 ([Power Tank](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Tank) or [Power Pack Module](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Pack_Module)) does not have a connected BMS or a [blanking plug](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loopback_Blanking_Plug) with [loopback](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS_CANBus_Loopback) wiring installed. |
| [36](#36) | Board 5V Error | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | MBB fault providing 5V micro-power (what's affected?) |
| [37](#37) | Board 3.3V Error | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | MBB fault providing 3.3V micro-power <br> Pre-2017 OBD-II affected - otherwise just a type of sensing feedback |
| [38](#38) | Idle Turn Off | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | The MBB timeout for detecting an idle control state has been activated, opening the contactor. <br> Reset by keying the bike off and on. |
| [39](#39) | [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) Out Of Range Disable | [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) | The throttle's electric signal safeguard is active |
| [40](#40) | BMS Throttle En Wire Disable | [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) | The throttle's enable wire safeguard(?) is active |
| [41](#41) | Low Battery Voltage Disable | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | The low battery voltage safeguard is active |
| [42](#42) | High Battery Temperature Status Disable | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | The high battery temperature safeguard is active |
| [43](#43) | Low Battery Temperature Status Disable | [Contactor Limits](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | The low battery temperature safeguard is active |
| [44](#44) | Kill Switch Disable | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | The kill switch safeguard is active |
| [45](#45) | Kickstand Switch Disable | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | The kickstand switch safeguard is active |
| [46](#46) | BMS Charger Connected Disable | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | The BMS checks whether the charger is connected, and this check failed. |
| [47](#47) | MBB Charger Connected Disable | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | The MBB checks whether the charger is connected, and this check failed. |
| [48](#48) | SEVCON Startup Disable | [Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) | The Sevcon controller startup failed and the resulting safeguard is active. |
| [49](#49) | Contactor Open Disable | [Contactor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Main_Contactor) | The contactor is open because of some safeguard (like 25 but not a normal indication). <br> Check other error codes and reset by keying the bike off and on. <br> Check logs later. |
| [50](#50) | BMS Self-Test Error | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | The BMS runs a self-test to decide whether it's safe to operate, and it failed. <br> Check BMS logs immediately. |
| [51](#51) | BMS Self-Test Warning | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | The BMS runs a self-test to decide whether it's safe to operate, and it succeeded but had a note. <br> Check BMS logs. |
| [52](#52) | Reserve Partition Disable | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | The MBB reserve storage partition(?) safeguard is active. |
| [53](#53) | BMS Internal Disable | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | A BMS internal check failed and the resulting safeguard is active. |
| [54](#54) | Internal Disable Error | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | An MBB internal check failed and the resulting safeguard is active. |
| [55](#55) | Internal Fault Error | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) | Could be anything? |
| [56](#56) | Monolith Not Connected | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | BMS#0 is just undetectable <br> (is this via CAN and voltage readings together?) |
| [57](#57) | Module Did Not Connect | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | The contactor didn't close? Or something more basic about the BMS (main, power tank, or module) reporting the battery unready. <br> Probably use the onboard charger to fix. |
| [58](#58) | BMS Sensor Warning | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) |  |
| [59](#59) | BMS System Warning | [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) |  |
| [60](#60) | Bike Configuration | [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) or [BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) | There may be an error in the bike configuration settings applied to the MBB and BMS. <br> Basically, they might have inconsistent model specifiers or battery size specifiers. <br> This has also been reported for incompatible firmware versions between the MBB and BMS. |

### [Isolation Faults](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Isolation_Faults)

*Isolation Fault* is jargon used on Zero Motorcycles systems to indicate a fault in some part of the system to isolate some HV electrical circuit from ground.

It can also mean the more specific condition where an attempt to locate the fault failed, an attempt to isolate the cause to a component or sub-circuit.

**Indication**

[BMS](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS) isolation faults are indicated by a combination of codes 20, 28, and 29.

**Meaning**

- On some part of the power system connected to the BMS at that moment, there is insufficient isolation (insulation) from ground.
- This can include anything on the 116V power cabling "bus".
- This is usually not a short, but can mean an imbalance that could compromise the bike's performance or safety.
- If left unattended to, it could deteriorate to a serious problem; in-build protections should shut down the bike prior to damage but this itself would be unsafe happening while riding.
- If the BMS reports a specific voltage in the logs with the isolation code, it means that a specific cell (the combined parallel cells at a particular level in the 28-cell series) has poor isolation to ground, roughly computable as "3.7V ⨉ N = logged voltage".

**Possible Aggravating Conditions**

- Damp weather
- Dust or mud ingress

**Troubleshooting**

1. Disconnect anything attached to the [Accessory Charging Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port).
   - If the condition clears, check the attached equipment (chargers and cabling) for grounding isolation.
2. Key the bike off and on slowly, waiting after each transition to see whether the condition clears.
   - If the error occurs without or before the contactor is shut, then the fault is within the battery and might be due to moisture or dust entering the front of the battery faceplate where the BMS is.
   - If the error clears after opening the contactor, then the fault is likely downstream of the contactor, including the Accessory Charging Port signal pins, the Sevcon controller, Sevcon DC-DC 110V->12V converter, and the MBB and DC-DC connections.
3. Check for moisture on the Accessory Charging Port signal pins and attempt to dry them as necessary.
4. After everything dries out and/or the isolation fault has disappeared apply dielectric grease to all connections that would be vulnerable to water ingres (under the seat, 12V connectors, etc)

**[Controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Controller) Hypothesis**

**Reference:** [via DoctorBass](https://www.facebook.com/groups/zmcowners/permalink/1546883172047552/)

It might be the Sevcon Motor controller that is defective.

The codes are related to BMS isolation fault - as an interpretation of a voltage present relative to the frame.

- A bad controller could have a single phase to the motor (M1, M2, M3 circuits) with a short to the heatsink.
- Apparently Sevcon and Zero are aware of this potential problem.
- The problem is apparently because the [Kapton](https://www.kaptontape.com/) tape they use between MOSFET transistors' heatsink and the aluminum heatsink might be punctured and create intermittent low resistance contact to the controller chassis.

Warranty replacements have been reported.

**Controller Isolation Diagnostic Procedure**

A dealer should be able to do this easily.

1. Key off the bike and wait 10 minutes for the system to fully discharge.
2. Remove the seat.
3. Uncover the top of the Sevcon controller.
4. Verify all inputs and outputs of the Sevcon controller are de-energized (zero/low voltage).
5. Disconnect the cables from the controller (M1, M2, and M3, the Ampseal 34-pin connector, and B+ and B- to be extra careful) and cover the leads for safety.
6. Check for continuity between each phase (M1, M2, and M3 terminals) and the controller heatsink plate.
   - If you get continuity (low resistance reading), then controller is defective.

[2018-05-03, Doctorbass confirms:](https://www.facebook.com/groups/zmcowners/permalink/1546883172047552/?comment_id=1656729414396260)

> I got these same errors couple month ago.. problem was the SR controller bad isolation from the phase output to the aluminum plate of his body. Controller replaced and that solved the problem.. no more 20 28 and 29 error code from now. The code talk about BMS but in fact the voltage level the controller bad electrical isolation create make the BMS to think it's the battery but in my case it was not.

**Isolation Diagnostics test**

1. Access the [MBB Console](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) terminal
2. Login via `login`
3. Execute the isolation test command with the *verbose* flag: `test isolation -v`

### Using Mobile App

See the [official mobile application](Official_Mobile_Application.md "Official Mobile Application") article.

### Diagnostics

- [Gen3/Log Messages](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3/Log_Messages)
- [Gen3/MBB Console](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3/MBB_Console)
- [Gen3/Error Codes](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen3/Error_Codes)
- [Brake Problems](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Problems)
- [Defective Wheel Bearings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Defective_Wheel_Bearings)
- [S Platform/Schematic](https://web.archive.org/web/2025/https://zeromanual.com/wiki/S_Platform/Schematic)
- [Gen2/Log Messages](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Log_Messages)
- [Gen2/Instrument Cluster/Troubleshooting](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster/Troubleshooting)
- [Gen2/Isolation Faults](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Isolation_Faults)
- [Gen2/Main Bike Board/Limitations](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Main_Bike_Board/Limitations)
- [OBD-II Port Location](https://web.archive.org/web/2025/https://zeromanual.com/wiki/OBD-II_Port_Location)
- [XMX Platform/Schematic](https://web.archive.org/web/2025/https://zeromanual.com/wiki/XMX_Platform/Schematic)
- [SDS Platform/Schematic](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Schematic)
- [Logs](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Logs)
- [How to build a cable to access the MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/How_to_build_a_cable_to_access_the_MBB)
- [MBB Software Reset](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Software_Reset)
- [MBB Hardware Reset](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Hardware_Reset)
- [ECMCables/OBDDROID Bluetooth Dongle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/ECMCables/OBDDROID_Bluetooth_Dongle)
- [ECMCables/OBDLINK USB Cable](https://web.archive.org/web/2025/https://zeromanual.com/wiki/ECMCables/OBDLINK_USB_Cable)
- [Gen2/System Warning Sequences](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/System_Warning_Sequences)
- [CAN Bus Diagnostics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/CAN_Bus_Diagnostics)
- [Gen2/Motor Controller/CAN Diagnostics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller/CAN_Diagnostics)
- [BMS Reset Procedure](https://web.archive.org/web/2025/https://zeromanual.com/wiki/BMS_Reset_Procedure)
- [Gen2/Error Codes](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Error_Codes)
- [DigiNow/Data Reaper Dongle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DigiNow/Data_Reaper_Dongle)
- [Gen2/MBB Console](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/MBB_Console)
- [Cycle Analyst](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Cycle_Analyst)

