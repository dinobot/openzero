---
title: "Common Problems"
source: https://zeromanual.com/wiki/Common_Problems
archived: https://web.archive.org/web/20250228133142/https://zeromanual.com/wiki/Common_Problems
captured: 2025-02-28
last_modified: "31 March 2020 03:35"
categories: ["Charging Symptom", "Wheel Sound"]
---

# Common Problems

## Overview

This is a basic troubleshooting guide, and also an indication that the symptom you're seeing is relatively common and has been thought about, often with some basic solutions.

## Behavior in wet weather

Avoid pressure-washing. Weatherproofing is much less effective against high pressure.

There are a few particularities of Zeros when they're exposed to excess moisture, particularly in heavy rain or after washing the bike.

### [Display Flicker](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Dash_Flicker)

The [dashboard](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster) can often be sensitive in wet conditions.

Occasionally it will display flickering or incorrect light indicators.

This will not affect normal operation of the bike and functionality should return to normal after drying out.

Applying electrical insulating grease to connections, or around the seal between the front face and back of the enclosure, might alleviate this.

### [Groan Sound](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belt_Groan_Sound)

The [belt](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt) in wet conditions will often make a pronounced new noise from when it's in dry conditions.

**Variations**

This thread describing a [loud buzzing sound on acceleration](http://electricmotorcycleforum.com/boards/index.php?topic=5785) has audio samples and discussion about how it occurs.

**Description**

This groaning noise has been called many things from a *Tie fighter* or a *Wookie* to a *water buffalo*.

**Effects**

It is completely normal and causes no ill effect on the bike, and will go away again when dry.

**Potential Causes**

The belt being dirty while wet may exacerbate this.

**Encoder Accuracy Hypothesis**

- There is a strong perception that the sound comes from the belt, but also an impression that the encoder sensors inside the motor lose accuracy in high humidity.
- This would make the controller think the motor is in a slightly different position, then send the wrong/displaced field to the motor, which would result in an oscillation.
- The motor might be driving the belt to resonate in this case.

**Potential Solutions**

- Wait for the bike to dry out.
- Silicone Spray

  Light application of a silicone spray to the motor shaft to the front sprocket should make it go away for months.

  | | |
  | --- | --- |
  | ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Ensure the spray doesn't have any petroleum distillates that will eat the belt materials. |

  The Encoder Accuracy Hypothesis above implies that one should apply it *near* the front sprocket to protect moisture from entering the motor housing.

**References**

[Groan sound : anybody having specific references for a pure silicone lubricant](http://electricmotorcycleforum.com/boards/index.php?topic=8705.0)

### [Loss of Traction](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loss_of_Traction)

The high torque of the electric powertrain can be an issue if you are not careful, especially on surfaces right after rain starts for the first times after a dry spell, as accumulated oil from vehicles has floated out of the pavement but not been washed away.

**Electric Powertrain Risks**

- The powertrain, once it breaks free of engaging with the ground, will spin up very quickly without quick operator reduction in throttle input.
- Re-engagement with a high difference in wheel speed to groundspeed can result in a jerky take-off or highside.

**Aggravating Conditions**

1. During takeoff

   When starting from a stop *especially into a turn*, the rear tire may slip above a certain torque.
2. While accelerating

   *Torque reduction* features in the bike programmed to make low speed take-off manageable may disengage in the 20-30mph range (32-48kph) and result in a loss of traction with no change in throttle input.
3. At speed

   The rear tire may slip when leaning into a turn or going over a bumpy and oily surface, initiating a fishtail.
4. On loose ground

   The rear tire may slip when engaged on loose gravel or sand, digging up the ground into a hole.

**Recovery**

- Ease off the throttle *very slowly*.
- Transfer your weight to the footpegs from the seat.
- Damp the oscillation through the handlebars, *loosely* to prevent initiating oversteer.

**Mitigation**

- If it rains after a long dry spell, Eco mode is worth trying because the torque roll-on rate is really low which means the onset of a slip can be recovered from without overreacting.

### Splash Protection

Zero motorcycle models have a rear wheel splash guard that protects the motor and the lower electrical areas under the seat, but the wheel can fling plenty of rain and mud onto the tail and on the back of the rider.

**Solutions**

[OEM Top Rack](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Zero_Top_Rack)

[OEM Rain Guard](Aftermarket.md#OEM_Rain_Guard "Aftermarket") applies to the tail extension; inexpensive but limited.

[Another mudguard?](Aftermarket.md#Mudguard "Aftermarket")

### Loss of Power

Power cutouts can happen at many levels.

#### [Loss of 12V Power](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loss_of_12V_Power)

Losing the entire 12V circuit can happen because the circuit is powered by a [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter).

**Related Confirming Symptoms**

- Headlamp, turn signals, and running/brake lights are *all* **off**.
- [Dash/instrument cluster](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster) is **on** and the bike **can operate**.

**Potential Causes**

- DC-DC converter-related:
  - High voltage input fuse to the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) is blown or disconnected.
  - Loose connector to the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter).
  - Enable signal failure between the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) and DC-DC converter.
  - General equipment failure of the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter).
- Broken ground/negative/return line in the 12V wiring bundle on the left side of the tank area.
- An [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) internal fault or error that results in no enable signal to the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter).

#### [Loss of Power to Motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loss_of_Power_to_Motor)

The onboard systems may cut off power to the motor and/or controller as a protective function if a fault is detected (whether real or misguided).

**Related Confirming Symptoms**

- On the dash, the green Driving Enabled light is **off**.

  If it is blinking or off, the contactor is open.
- Check the dash for [Error Codes](Error_Codes.md "Error Codes"):

  **20, 28, and 29**: [Isolation Faults](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Isolation_Faults).

  **44**: Engine cutout switch.

  **45**: [Kickstand Sensor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Kickstand_Sensor).

  **39**: [Throttle](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Throttle) reading high or low.

  **42**: Battery high temperature.

  **43**: Battery low temperature.

**Potential Causes**

- Moisture on the [Accessory Charging Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) signal pins.
- A problem with the [controller](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Motor_Controller) per the [isolation fault](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Isolation_Faults) guide.

**Troubleshooting**

Mostly, check the [Accessory Charging Port](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Accessory_Charging_Port) while on the road.

- Confirm that the rubber boot/cover on the accessory charging port is in-place.

  The accessory charging port comes with a rubber boot/cover.

  This circuit is low voltage so not dangerous, but loss of power while riding can be dangerous.
- If the motorcycle cuts out in the rain or shortly after, check whether the connector is covered properly and try to dry it out.

  Pull off the boot and shake it free of moisture while the bike is keyed off.

**Recommendations**

- Leave the Accessory Charging Port boot cover in place *when not in use*.
- *If the motorcycle exhibits cutouts in the rain*, apply dielectric grease to vulnerable connections.

  This hopefully reduces the chance of shorting or the appearance of a short.

### [Power Cutout Failure](https://web.archive.org/web/2025/https://zeromanual.com/wiki/12V_Power_Always_On)

When the entire 12V circuit stays, *despite* keying the bike off and disconnecting charging sources.

This may be continuous or intermittent.

**Related Confirming Symptoms**

With the ignition is keyed **off**, the key removed, and the bike unplugged from charging sources:

- Headlamp and running/brake light are *both* **on**.
- [Dash/instrument cluster](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Instrument_Cluster) backlight is **on** but the bike **does not operate**.

**Potential Causes**

- [Ignition Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Switch) is faulty.
- [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) is faulty.
- [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) is faulty, sending an enable signal to the DC-DC converter.

**Risks**

This will slowly drain the battery.

A continuous use of the headlamp might drain the battery in a week's time or less.

Time to discharge (hours) = SoC (%) / 100 × capacity (kWh) × 1000 / 55W.

If the condition is a result of a short circuit around the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter), it may over-discharge the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB), causing failure of that critical component.

So try to diagnose and solve this problem as soon as possible!

**Troubleshooting**

1. With the bike keyed off, check the voltage across the [Ignition Switch](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ignition_Switch), *or* check if the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) is on and whether it reports in the [console](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) that the ignition switch is shut.
2. With the bike keyed off and unplugged, access the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) connector with a voltmeter that has needle probes.

   On the [SDS Platform](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform), you'll need to [remove the board mounting plate](https://web.archive.org/web/2025/https://zeromanual.com/wiki/SDS_Platform/Board_Mounting_Plate_Removal).
3. Verify the battery [State of Charge](https://web.archive.org/web/2025/https://zeromanual.com/wiki/State_of_Charge) via input/bus voltage:

   Check voltage present between (+) pin 2 and (-) pin 3.

   This should be between 95V and 116.2V, and roughly indicates [State of Charge](https://web.archive.org/web/2025/https://zeromanual.com/wiki/State_of_Charge).
4. Test whether the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) is sending the enable signal:

   Check voltage between (+) pin 1 and (-) pin 3.

   If this is *zero*, then the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) is **faulty** independent of the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB).

   If this is *not zero*, then the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) is enabling the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter), and is **faulty**.
5. Confirm output from the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter):

   Check 12-14V present between (+) pin 4 and (-) pin 5.
6. Test whether the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) responds to the enable signal:

   Connect pin 1 directly to pin 2 using a piece of cable.

   Connect power to (+) pin 2 and (-) pin 3.

   This should transmit high voltage to the enable input at pin 1, and should make the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) work if it is functional.

If the [DC-DC 12V Converter](https://web.archive.org/web/2025/https://zeromanual.com/wiki/DC-DC_12V_Converter) is faulty with the [MBB](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB) okay, then the bike should run normally, but with a [Loss of 12V Power](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loss_of_12V_Power).

## [Loss of Range](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Loss_of_Range)

Zero [range](https://www.zeromotorcycles.com/range/) can vary remarkably more than a gasoline-powered vehicle, which takes time to understand.

Zero range estimates are accurate *for the conditions stated*.

First, consult Zero's [Range page](https://www.zeromotorcycles.com/range/) for factors that change real-world range.

**Related Confirming Symptoms**

- [Power Reduction](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Power_Reduction) at higher SoC levels.
- Lower range estimates for a given SoC reading, especially near 100%.

**Potential Causes**

- The majority of range loss is due to the effects of cold weather on the battery.
- Internal resistance increases in batteries at low temperatures.
- Rain will exacerbate the problem since thermal transfer will be higher with water contacting the battery case.
- The [official manual](Official_Owners_Manual.md "Official Owners Manual") has a section for Cold Weather specifically calling out that up to 30% of range might be reduced at 30F ambient temperature.
- The effect is roughly linear below (say) 45F ambient temperature.
- The [internal resistance](http://batteryuniversity.com/learn/article/discharging_at_high_and_low_temperatures) of the battery is the primary mechanism for reduced performance.

**Recommendation**

If full range is required at low temperatures, wrap the battery in a suitable insulating material in cold seasons.

Neoprene at 1/16" thickness has been tested at highway speeds to make a marked difference in battery temperature (but not to an unsafe degree).

Cover the front of the battery primarily and the forward halves of the sides.

Make sure to securely fasten the neoprene so it will not get caught in the front wheel.

Grommeted holes can be used to secure the wrap through the central frame tube and the tank plastics.

A thin (3mm or 1/8") sheet above the battery would also help in cold precipitation.

Masking tape across the front face has also been used effectively.

| | |
| --- | --- |
| ![Warning](../images/Attention_Warning_Icon.png "Warning")  **Warning:** | Any wrap used to insulate the battery at low temperatures will prevent sufficient cooling for it to operate at normal temperatures. Remove any wrap when operating above 45F. |

**Advice/Experience via [Zee in Northern Ontario](http://electricmotorcycleforum.com/boards/index.php?topic=7431.msg62019#msg62019)**

> Well this Canuk is a heavy sled (snowmobile) head and lives in northern ontario and owns 2 Zero's 2010MX & 2015FX and rides all year long as long as the roads are clear.
>
> - The bikes are stored in a non heated garage and it takes full battery awareness and charging smarts to keep everything going all winter.
> - The temperature inside the garage is usually 10C warmer then outside.
> - I automatically plug every bike in after every discharge when the batteries are still warm so the FX is usually fully charged when I start a ride.
> - When I decide to go for a ride and it is -20C outside
>   1. I will first go for a 20% discharge were the bike will run like a lame duck.
>   2. Then I will put the bike back on charge with extra charger while the batteries are warmed up
>   3. When the bike is back at full charge then the bike wakes up a bit but still not at full summer power but enough power to tickle my fancy.
>
> I can't wait for battery technology to advance so I can covert my sled (snowmobile).
>
> - Also be aware that the battery will shut down with up to 20% power left if you are pulling steady on it in the cold weather :) cheers

## Weak power in cold temperatures

From EMF:

> ... higher internal resistance of the battery at colder temperatures causing current limiting, ... It can be a little disconcerting when this happens right as I am trying to overtake slower vehicles.
>
> You can even see that in the logs.
>
> You'll see entries "discharge current limited (XX%)".
>
> That tells you the percentage the power (=battery current) has been limited to, because of the high voltage sag due to higher internal resistance because of the cold.
>
> Right behind that you will read a "MinCell" entry
>
> this one tells you which cell was the weakest and caused the limitation and with what voltage.
>
> The limitation of power is directly related to topspeed, as you need more power the faster you ride.

## Charging

### [GFCI](https://simple.wikipedia.org/wiki/GFCI) Faults

Ground fault circuit isolation outlets detect unequal currents across the hot to neutral prongs.

The [Onboard Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) tends to aggravate these detectors, particularly if paired with another load on the same circuit phase in a household or building.

**Recommendation**

If GFCI faults occur regularly, charge the bike without a ground connection:

- Use a [cheater plug](https://en.wikipedia.org/wiki/Cheater_plug) to mask the Zero's three-prong plug as a two-prong ungrounded plug, or
- Just break off the grounding prong in the cable plug with a pair of pliers.

### [Blinks 4 or 5 times and fails to charge](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Charge_Failure_After_Blink_Sequence)

When the charge indicator blinks 4 or 5 times, and charging fails to start.

**Cause**

The charging fuse could be blown.

**Recommendation**

Find the charging fuse in the wiring harness, remove it from the heat shrink, and replace it.

It is unclear whether a resistance check can be easily performed to save time troubleshooting, but a voltage check should work.

- ![](../images/Harness_with_charging_fuse_1.jpeg)

  Harness with charging fuse inside heatshrink
- ![](../images/Harness_with_charging_fuse_2_cut_open.jpeg)

  Harness with charging fuse, cut open
- ![](../images/Harness_with_charging_fuse_3_cut_open.jpeg)

  Harness with charging fuse, cut open, back

**Owner Comment**

> SF Moto took 1.5 hours troubleshooting and then replaced the entire harness. Total cost about $650. The fuse is inside the thick heat shrink.

### Stuck/Warm Charging Cord

From [this thread](http://electricmotorcycleforum.com/boards/index.php?topic=5778.msg45518#msg45518), there's a [good explanation](http://electricmotorcycleforum.com/boards/index.php?topic=5778.msg45529#msg45529) of what can cause a power cord to get stuck/fuse.

Most charge cord recommendations focus rightly on wire gauge and length to avoid heating. A stuck cord/plug on the other hand will be due to the connectors fusing together, possibly after years of use, so it's a connection that has deteriorated to the point where it generates its own heat.

**Note**

If you are using a cord that does not meet Zero's requirements, the cord or particularly the plug may not be rated for the current (12A continuous at least), and will overheat for that reason.

**Recommendations**

- Clean the contact prongs on the motorcycle's receptacle. Use something specialized for the purpose.

  Road debris or just dirt on the prongs can increase electrical resistance and produce heat that weakens the cable plug.
- Try to avoid bending the blades of the male connector whenever possible.

  They should be fairly well annealed brass but they will eventually fatigue.
- One preference is to have them bent inward slightly.

  That gives a little bit of pressure between the blade and the socket which helps provide a low-resistance connection.
- Keep an eye on the strain relief on the backside of the connector.

  If you see cracks starting to appear, you might want to replace the cord or at least get a backup so you won't be left without one when it fails.
- Be sure to always grab the molded part of the connector when disconnecting, rather than yanking on the cord.

  Especially when the cable is warm and soft, that's a great way of pulling it apart.

### Charging Errata

**Charging light stays on after completion (2017 model year)**

"...prior to 2017 models, the green charge indicator did go out once the bike was unplugged. For 2017 though, a component was deleted, so the light stays on until voltage in the circuit bleeds off, or the contactor is closed."

Source: [Re: Zero SR 2017. New model startup issues or just my bike?](http://electricmotorcycleforum.com/boards/index.php?topic=6824.msg63673#msg63673) Electric Motorcycle Forum user **droidish** reports on the charging indicator staying on after completion)

### [Faulty Calex onboard charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Calex_Charger/Faulty_Operation)

**Charging stops below 100%**

- A defect in the onboard charger (due to spikes on the canbus?) cause charging process to stop prior to reaching 100%.
- Even when left plugged in the SOC will no longer reach 100% and will keep decreasing over time (next charges).

**Collateral Damage Risk**

If a bikes has damaged the charger it is likely to damage the replacement charger over time as well.

**Actions**

The onboard charger is not repairable beyond checking the inlet

A replacement guide for the onboard charger can be found here [Calex Charger Replacement](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Calex_Charger_Replacement).

## Frame/Body Panels

Prior to 2017, [Zero's plastic panels](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Bodywork_Material)' color is molded-in and will fade with exposure to the sun over a year or two.

The battery casing will also acquire a mild kind of patina over time if left sun-exposed over a very long time.

## Front Wheel/Suspension/Steering

### Fork Oil Leak

Sometimes the front fork seal can leak because it gets dirty. [One recommendation](http://electricmotorcycleforum.com/boards/index.php?topic=5748.msg42549#msg42549) is to keep a handy tool for cleaning it out quickly. [SealMate](http://sealmate.net/) has been recommended but other solutions can be equivalent.

**FastAce Left Fork Leak**

The FastAce front forks for the 2013 (and possibly 2014) are known to sometimes develop a weep/leak on the bottom of the left tube.

The vaguely-communicated cause is the asymmetric strain of the single brake disc on that side, combined with a lack of compensating setup when installing the tubes.

Zero tends to include this issue under normal warranty coverage, to replace the tubes, if the forks themselves develop the problem less than a year after having installed them.

### [DS/FX Front Brake Line Obscures Dash](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Gen2/Armored_Front_Brake_Line_Rerouting)

**Goal**

- The DS and FX have an armored front brake line with ABS wire clipped onto it that runs in front of the handlebars.
- It usually obscures the ignition but sometimes the lower part of the dash display.
- 2017 models' design resolves this.

**Motivation**

It's okay to re-route the cable or use some strap (zip tie or hook-and-loop) to pull it towards the handlebar to clear up the cockpit.

**Steps**

1. Remove the 4 dashboard bolts.
2. Remove the 2 headlight bolts.
3. Push dashboard through loop in brake line.
4. Unplug the 2 headlight wires.

   The main connector is tight; it's easier remove the bulb, but don't touch it.
5. Put the brake line on other side of headlight wires.
6. Replace the headlight wires.
7. Wire-tie the ABS wire plug to the larger plug behind the dashboard, so it doesn't dangle.
8. Replace the dashboard with 4 bolts.

   ![Brake1.jpg](../images/Brake1.jpg)
9. Observe the arc of the brake line.

   Is it forming too tight an arc? Move it if so.
10. Turn the handlebar to its extremes, and observe the brake line.

    Is it being pinched, or rubbing against anything sharp? Use zip-ties to hold it away, if so.

    ![Brake2.jpg](../images/Brake2.jpg)
11. Compress the front forks (lean on bike), while moving handlebar to extremes, and observe brake line.

    Is it rubbing against anything sharp?
12. Repeat until you're satisfied there is no way the brake line is endangered.
13. Bolt on the headlight.
14. Perform a final check (turning the handlebars and compressing the forks) for abrasion.
15. Test drive: go up/down curbs, or otherwise compress / test range of motion.

## Rear Wheel/Suspension/Belt

If the rear wheel leaves the surface under acceleration, it can accelerate rapidly, overstressing the belt when landing. Belts have been reported broken, leading some to switch to noisy chains instead. Take care with potholes and speed bumps, it you leave the surface, lay off the throttle to avoid damaging the belt.

### [Defective Wheel Bearings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Defective_Wheel_Bearings)

Some models suffered from defective wheel bearings.

Usually these bearings should last 80,000+ miles, but some owners have reported much lower lifetimes (10,000 miles).

**Symptoms**

- Snapping / clicking / popping sounds. This noise is typically heard when cornering or making sharp turns.
- Grinding when the vehicle is in motion. The noise is normally heard when turning or when there is a shift in load.
- Sharp strike (as if someone struck the wheel with a hammer) accompanied by a grinding sound.

**Related Symptoms**

The noise / vibration will vary depending on the load / resistance applied to the weel.

It might disappear when the motorbike is on a lift (in this case, using the brake of the damaged wheel could help applying enough resistance for the noise to appear).

### [Noisy Belt](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belt_Noise)

The belt often makes various noises while riding that sound vaguely concerning.

These noises should be investigated.

**Potential Causes**

- Belt misalignment.
- Debris between the belt and sprocket.

**Effects**

If the belt is misaligned, it may be under asymmetric loading, and fail early and badly.

If the belt is encountering debris, it may fail early and badly.

**Potential Solutions**

- Check the belt and sprockets for debris and clean them with a non-abrasive brush.
- See the [Belt Adjustment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belt_Adjustment) procedure.
- Fine tune where the belt rides on the rear sprocket.

  [this FB post by Paul Murray](https://www.facebook.com/photo.php?fbid=10210641031081262&set=p.10210641031081262&type=1&theater) suggests this method for dealing with belt noises.

1. Adjust the belt tension screws on the back axle so the belt tracks just barely off the side lip.

   The side lip was rubbing the side of the belt and making noise.
2. Loosen the axle nut so the tensioners can move the axle freely.
3. Adjust the belt tension with the sprocket side tensioner and keep the brake disc side even, using the brake side tensioner screw.
4. Use the alignment notches on each side as a reference.
5. Then, with the rear wheel off the ground, spin the back wheel by hand.

   Using the accelerator is sketchy and spinning by hand will probably do the job.

   Observe where the belt is riding.
6. Adjust the brake side tensioner a 1/4 turn (or less), in or out, and spin the wheel again.

   Observe where the belt is tracking.

   As you do this a few times you will see the belt move from side to side.

   When you find the spot where the belt tracks just off off the side lip, and the tension is correct, that is the happy spot!

   That should eliminate some belt noises.
7. Tighten up the locking screws on the tensioner bolts, and tighten the axle nut when finished.

| | |
| --- | --- |
| ![Disclaimer](../images/Attention_Warning_Icon.png "Disclaimer")  **Disclaimer:** | I am not a motorcycle mechanic, but using the notches for axle location is just not accurate enough for belt tracking. |

- Replace the belt with a loose chain drive, where such alignment is not an issue.

### [Rear Vibration](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Wheel_Vibration)

Rear wheel vibration may occur after tire replacement.

**References**

[Vibration after rear tire replacement](http://electricmotorcycleforum.com/boards/index.php?topic=6041)

**Troubleshooting**

- Check for any play in the wheel relative to the swingarm, which would suggest a [bearing issue](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Rear_Bearings_Replacement).
- Check for any play in the swingarm relative to the frame, which would suggest a [swingarm](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Swingarm) mount issue.
- Check for and fix any [belt alignment](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Belt_Alignment) issues.
- Check for [motor](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Motor) mount play, front sprocket play, or check MBB logs for motor-controller encoder alignment issues.

**Preventative Measures**

- Check for wheel balance after a tire replacement.

  Balancer stands and compensating weights are commonly available; whoever changed the tire should have done this.

### [Belt Damage](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Drive_Belt/Damage)

**Bumps**

Belts are most commonly damaged by using the throttle in the moment that a wheel becomes airborne, over a bump at speed, say.

If the wheel spins up momentum in the air, regaining traction on landing will jerk the belt, causing a loss of belt teeth or the belt may snap entirely.

**Debris**

Gravel, road debris, or sand can damage or snap the belt if caught between the belt and the sprocket.

Sand seems to be the most sure to destroy a belt; gravel has a lower probability given some basic design protections that should scatter gravel out of or away from the sprocket.

**Teeth loss tolerance**

Missing belt teeth can be tolerated briefly until a replacement can be made by riding at low torques (easy acceleration, not too high sustained speeds).

The front sprocket has up to 28 total teeth, and only half of those can be in contact with the belt at any given moment, so a continuous sequence of stripped belt teeth might continue up to perhaps 12 but any length of missing teeth is riskier as it gets longer.

The teeth and inner surface of the belt can melt into the front sprocket if the sprocket slides where there are not teeth

If the front sprocket slides, the front sprocket will go fast and it will take out additional teeth as the wheel catches up

Eventually you will have to remove material from the front sprocket or replace it. And eventually the belt will break and you will be unable to climb a San Francisco hill (does this sound oddly specific?)

Scraping out the material with metal can damage the sprocket. Avoid it. A hardwood dowel or a polycarbonate rod, sharpened, is better. Acrylic is too weak.

## Brake System

### [Brake Squeal](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Squeal)

This is a common sound on Zero motorcycles, for reasons which have never been decisively explained.

**Related Confirming Symptoms**

- Usually occurs only when pressing on the brake lever or pedal. Rarely occurs at specific speeds when brakes are not pressed (the pad(s) are resting on the caliper).
- Vibration felt through the brake lever or pedal when squealing.

**Effects**

- Brake performance seems *technically* unaffected.
- As the loudest sound from the vehicle, this can be unnerving for rider, passenger, or onlookers.

**Potential Causes**

This was more common on 2013-2014 models which had cheaper / lower spec [Brake Systems](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Brake_Systems).

This suggests a design issue between the disc and calipers that tends to produce resonance the way the pad is mounted.

**Potentional Solutions**

- [LocTite Disc Brake Quiet stick applicator](http://www.loctite.ph/php/content_data/LT4246_disc_brake_quiet_stick11.pdf) or silicone grease for the backs of the pads.
- [Apply water to the calipers after a ride](http://electricmotorcycleforum.com/boards/index.php?topic=8128) seems to eliminate squeal for about a week or so.
- Camfering pad edges.
- If *the bike is new and brake squeal is constant*:

  Bed the brakes per the [Official Owners Manual](Official_Owners_Manual.md "Official Owners Manual") and then give the bike a gentle wash.

### Regenerative Braking

When starting with a full charge, downhill, with a mode that does regenerative braking, you may feel a pulsing, as the regenerative braking repeatedly engages and then disengages so as to not overcharge. 2015 and newer versions of the firmware appear to soften or eliminate this effect. Using sport mode intentionally for the length of a block appears to be enough to start using regenerative braking.

Regenerative braking is only enabled in the speed range of about 8 mph to 70 mph (could vary slightly depending on model). If you go faster or slower, even in a mode with regeneration enabled, it will not turn on until your speed falls within that range.

When braking, it can be effective to apply the brake lightly, just enough to activate the taillight, well ahead of time. This minimizes brake pad wear while improving range (in Eco mode or Custom mode, depending on regenerative braking settings).

### Parking on Hills

Lacking a clutch and transmission, a Zero offers no built-in support for preventing a parked motorcycle from rolling downhill.

Solutions:

- [OEM brake lever lock](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_4&products_id=205)
- Double-sided velcro loop.
- [Grip Lock](http://www.webbikeworld.com/r2/motorcycle-lock/grip-lock/) is a security device for locking the throttle and front brake.
- [Zero Parking Brake Kit](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_4&products_id=243)

  The 2017 Owner's Manual explicitly describes a Parking Brake accessory and shows how to operate it (paddle on the right handlebar side that operates a rear brake caliper).

  It became available in mid-2017 but seems to fit 2014+ S platform models and 2015+ X platform models.

## Motor/Controller

### Low SoC

For 2014 and earlier S/DS/SR models, power is reduced below 15% battery charge, and may cut out at or below 10%.

The controller is definitely reducing power to protect the battery when its voltage is reduced.

One point of confusion is why power cuts back before 0%. It may to be due to individual cels being fully discharged too soon. Turning the bike off for a minute and then turning it on may allow using the bike for a few more miles at very slow speeds and power in order to limp home, because the lowest cel should temporarily rebound in voltage enough to satisfy the battery protection logic even though the cell will not produce power and will strongly limit what can be done with the battery until recharged.

Models with fewer battery bricks like the FX will cut back power much sooner near 50% battery charge because each cell has a greater impact on the entire power pack.

2015 models experience this trouble less acutely, and 2016 models seem willing to continue travel at 0% for up to several miles. The implication is that the cells are much more robust in these battery generations, and an abnormally low individual cell is very unlikely.

If there is an emergency need to operate to motorcycle this way, use the battery voltage display in the mobile app to understand how far away you are from the battery being completely unusable.

In any case, running the battery charge this low should be followed immediately by charging to prevent damaging the battery, and it may reduce overall battery lifetime if performed regularly.

### [Overheating](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Overheating)

After "spirited" riding especially on an SR or a DSR a temperature icon may flash, indicating high temperature. If temperature continues to build it will go solid (p. 4-14 [2014 Zero SR owners manual](http://media.zeromotorcycles.com/resources/owners-manuals/2014/2014-Zero-Owners-Manual-S-SR-DS.pdf))

**Pre-2012 Recommendations**

On pre-2012 models, it is important to slow down and let the motor and electronics cool as there are no inbuilt protections.

**2012+ Recommendations**

On 2012 and newer Zeros, the controller will automatically reduce phase current as the motor heats up which reduces performance and motor heat.

This gets more aggressive as motor heat increases until power is reduced to a point where the motor is shedding heat as fast as it can generate it.

The 2014 and newer SR and DSR motors have higher temperature magnets, and it is normal to see 120+C under spirited riding.

**IPM Design Factors**

The 2016 SR/DSR/FXS motors (and S/DS motors for 4-brick variants) have an interior permanent magnet (IPM) design that reduces the heat produced and reduces the stress from heating by distributing the heat generated, so they appear to operate cooler in the same conditions for longer periods of time.

It has been said that with an IPM motor, the controller becomes the limiting performance factor.

**Battery Overheating**

Repeated iterations of highway riding and rapid charging can cause battery overheating.

The contactor opens up above 50C, preventing charging or operating the bike.

Once you are stopped, without airflow on a hot day, it may be difficult to proceed for some time.

**Recommendations**

- Slow to 55-60 mph for the last miles before charging is reportedly enough to cool the battery enough to allow rapid charging.
- Reduce charging rate to at or near 4kW (or 0.4C) to minimize the heating produced while charging.
- Disengage the onboard charger while charging, since the heat it produces conducts directly into the bottom of the battery case.

Year over year, newer battery designs have lower internal resistance and tend to produce less heating internally so will perform better.

## Battery/Chargers

### Hot Weather Charging

On a hot day, or with rapid chargers, the battery may get hot when charging.

**Recommendations**

- You can use the app to detect this condition.
- Charge in the shade, when possible, with good ventilation.
- A half cover or stretch-cover can help make shade.

## Electrical System

### [Hazard Lights Interfere With Turn Signals](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Hazard_Lights_Interfere_With_Turn_Signals)

On 2016 models, the turn signals can stop working when the hazard lights are engaged.

**Conditions**

While either left or right turn signal are engaged:

- If you hit the hazard switch while the *dash turn signal indicator* is **off**, the circuit will lock out.

  It can only be reset by canceling the turn signal.

If you time it so you engage the hazard indicators while the *dash turn signal indicator* is **on**, the circuit will work normally.

**Avoiding**

Hopefully rarely will you need to use the hazard indicators while a turn indicator is engaged.

If you do need this, cancel the turn signal before you hit the flasher button (or you stand a 50% chance of locking up the circuit).

**Fix**

1. Turn off the hazard lights.
2. Reset the turn signal.

**Reference**

[Blinking switch malfunction](http://electricmotorcycleforum.com/boards/index.php?topic=6983)

## App and Bluetooth

See the [Official Mobile Application](Official_Mobile_Application.md "Official Mobile Application") page under [Common Problems](Official_Mobile_Application.md#Common_Problems "Official Mobile Application").

