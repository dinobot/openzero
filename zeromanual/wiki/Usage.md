---
title: "Usage"
source: https://zeromanual.com/wiki/Usage
archived: https://web.archive.org/web/20241125165855/https://zeromanual.com/wiki/Usage
captured: 2024-11-25
last_modified: "29 April 2020 18:36"
---

# Usage

This covers topics about using a Zero specifically as a vehicle.

## Washing

First, see the **General Maintenance: Cleaning** section of the [official owner's manual](Official_Owners_Manual.md "Official Owners Manual").

Do *not* pressure-wash or use a directed spray on your bike.

**Risks**

Even just a water spray directed at the bike can randomly place water in sensitive areas that can cause corrosion or electrical faults that a gas motorcycle is not sensitive to.

This risk is not accounted for by regular waterproofing; [IP Code](https://en.wikipedia.org/wiki/IP_Code) ratings apply to weather, which assumes specific characteristics that even a garden hose can accidentally violate.

Dielectric insulating grease (protecting the BMS and other connections) can be deformed and made ineffective by directed force through a water stream.

The pins on the accessory charging port above the motor can induce a fault if water gets on them in certain ways, and a forced water stream can achieve this even with the protective rubber boot in place.

### How to Wash

Use a sponge or soft cloth with mild detergent and plenty of water.

Apply the water from a bucket with the sponge or cloth, or with a light-duty manual spray bottle.

Lint-free sponges or cloths will tend to preserve plastic surfaces better, and avoids adding grit near belt teeth or hardware.

### What to Wash

**Plastics/Bodywork**

Use a lint-free rag or sponge to avoid marring the plastic surface.

**Belt**

A soft brush (applied to the rear sprocket mainly) can remove accumulated road and tire debris from between the sprocket and the belt teeth.

This debris no matter how fine puts pressure on the belt and, depending on perspective, adds to its wear and decreases its lifetime or increases its risk of failure.

Via official the manual: *Clean the belt with mild soap and water when washing your motorcycle*.

## Commuting

### Range Estimation

Test your bike on your commute! Make a projection by going halfway and checking battery state of charge.

**Considerations**

How hilly your route is or how fast you have to go will increase your power requirements per distance.

Harsh or cold weather or strong headwinds will also increase your power requirements (up to say 20%) per distance, *seasonally* or just temporarily.

### Charge Cycle Plan

Develop a charge cycle plan based on what your commute actually uses.

| Round-Trip Consumption | Charge Recommendation |
| --- | --- |
| <=40% | Charge every other day |
| 40-80% | Charge daily |
| >=80% | Charge twice daily (after each leg) |

Charging less often is motivated by the finding that 100% SoC maintenance retains charge capacity less well over the battery's lifetime.

### Home Charging

Make sure you can easily plug in all the time.

- Running a cable up to a second story apartment every night could be tedious; find a way to make an easy routine.
- A garage both helps deter theft and avoid freezing winter conditions which impact the battery and charging overnight.

**GFCI**

If your household circuit has ground fault isolation features ([GFCI](Common_Problems.md#GFCI_Faults "Common Problems")), the charger may trip that circuit.

It seems to be fine to break off the ground pin of your charge cord or use a cheater plug to avoid connecting charger ground to household ground.

**[Limiting Current](http://electricmotorcycleforum.com/boards/index.php?topic=6919)**

If you need an S/DS bike to draw a lower current from a circuit because it unavoidably shares it with other household items, an external [OEM Quick Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Zero_Quick_Charger) will only draw 9A instead of 11-12A at 110V.

Alternatively, using a plug adapter from 220V into the [Onboard Charger](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Onboard_Charger) will mean that the charger uses <7A at 220V which can also be easier to deal with.

### No Home Charging

If you can't charge at home, try to ensure your motorcycle has enough capacity so that each leg is under 30%, so that 30-40% excess is always available for errands or short weekend trips.

This might involve taking a slower or less hilly route on your commute, as range drops off at higher speeds.

Zero recommends not letting the battery rest below 30% state of charge, which is also a factor in battery life worth considering.

**References**

[Apartment/Condo dwellers - what to do if you cannot charge at home](https://greentransportation.info/ev-charging/range-confidence/chap6-home-charging/apartment-dwellers.html), a guide by David Herron.

[Only charge at work?](http://electricmotorcycleforum.com/boards/index.php?topic=5970) forum discussion

### Outdoor Storage

If the bike won't have a regular indoor storage location, try to keep it under cover with some ventilation to prevent moisture accumulating.

Mind the maintenance recommendation to apply dielectric grease around all exposed electrical junctions and entryways that could lead to circuit damage over time.

Also mind temperature extremes and their effect on charging.

### Workplace Charging

You'll want to (and maybe have to) charge at the workplace; asking is a good idea to avoid conflict. A calculation of the cost of the power involved (very low) should help frame how little is involved.

### Opportunity Charging

This basically means charging as a habit whenever stopped for an errand.

See [EV Charging](EV_Charging.md "EV Charging") for an in-depth look at this skillset.

There's a skill to build of knowing where to expect available power outlets, like parking garages or the sides of restaurants. [PlugShare](https://www.plugshare.com/) is a particularly good service to update when you find a new charging opportunity.

There's also the etiquette to not present this conspicuously in case it irritates a business owner. Try not to interfere with someone's workplace or run a cord across a well-trafficked path.

## Extreme Temperatures

### Hot Weather

The maximum power pack internal charging temperature is 122°F (50°C). The contactor will open at that point.

| Factor | Impact | Mechanism | Recommendations | Result |
| --- | --- | --- | --- | --- |
| Onboard charger | Heating | Mounted directly to the bottom of the battery pack; transmits its waste heat | Use an external charger without the onboard charger | (Used Successfully) |
| SoC | 〃 | Charging or discharging above 80% or below 20% will meet increased internal resistance | Charge from 20% to 80% only | (Used Successfully) |
| 〃 | 〃 | 〃 | Reduce speed operating below 20% |  |
| Charge Rate | 〃 | Charging above 0.4C will generate heat within the battery | Keep charging at or below 0.4C total <br> Power Tank upgrade will raise C rate <br> Newer year batteries have reduced internal resistance | (Used Successfully) |
| Discharge Rate | 〃 | Discharging above 0.4C will also generate heat within the battery <br> (corresponds to 45mph for a stock 4-brick bike with no drag reduction) | Drive more slowly | (Used Successfully) |
| 〃 | 〃 | 〃 | Use a good windscreen | 5-15% |
| 〃 | 〃 | 〃 | Adopt a fairing | 10-25% |
| Direct Sunlight | 〃 | Sunlight will heat the battery case | Shade the battery case while charging | (Used Successfully with Kwikover) |
| 〃 | 〃 | 〃 | Ride early or late in the day | (Used Successfully) |
| Airflow | Cooling | Air carries heat from the case surface by conduction | Operate at consistent slow speeds (55mph or down to 45mph) to get the most airflow over the battery while minimizing current due to drag | (Used Successfully) |
| Water flow | 〃 | Water carries a lot of heat from the case surface by conduction and evaporation | Use a hose on the battery case with a spray or mist setting while charging | (Used Successfully) |

**Ideas**

It is conceivable that adding surface area to the battery casing could improve cooling effects at speed, but this is not yet explored.

Forced cooling with ice or water over the case would require a loop through a radiator to be effective, but a water hose with a spray nozzle should help.

**Discussion**

[Re: ugh battery overheating](http://electricmotorcycleforum.com/boards/index.php?topic=7213.msg60062#msg60062) by Terry Hershner

### Cold Weather

For riding in cold climates or through a winter that gets to or below the freezing point, there are a number of concerns, mainly keeping the battery temperature above its minimum.

The manual recommends not running the bike if the battery temperature is below 23F/-5C, and then if you do, immediately put the bike on a charger once its temperature is raised to 32F/0C. The BMS will open the contactor at -22F/-30C per Farasis' recommendations.

**Aerostitch "Zero Below Zero" experiment**

Aerostitch ran a blog detailing how they used a Zero FX through Duluth, MN's winter. Some highlights:

- [Preparations](http://www.aerostich.com/blog/zero-winter-test-bike-preparation/):
  - Heated grips
  - Battery heating blanket, like a heated vest using an SAE connector.
  - Extra 12V connections for heated gear.
  - Temperature gauge mounted on the dash but linked to the battery case.
  - Studded tires.

Since charging and operating the bike generates a certain amount of heat, an insulating jacket could help retain battery heat at speed.

**Insulating Jacket**

Brian Rice ran a test wrapping ¼” thick Neoprene around the front and sides of a 2013DS power pack battery compartment.

**Securement**

- Two grommets at the rear upper corners, with a bungee running through the center frame tube.
- Two grommets on the upper edge of the wrap, placed to hook inside the "horns" of the tank plastics.

**Effectiveness**

Range (and energy consumption) appears to return to normal in 40F weather.

Measurements are gross due to limitations in 2013 dash readings; MBB logs and app SoC endpoint readings for mostly equivalent conditions (very similar daily temperatures and weather) were used over a 80 mile round trip.

Battery pack surface temperature was noticeably warmer to the touch after the ride.

Testing in a cold wet rain would prove this out further; might indicate a need for a wrap extension to divert rain from sitting on the battery pack under the tank plastics.

**Ingo Sch > ‎Zero Motorcycles Owners Group**

"After beeing limited two days in a row to 145kph at 6°C and 128kph at 5°C I installed a neoprene insulation at both sides of the battery. The last 3 days I could go with full 162kph at -2°C and around 150kph @-5°C. Works great, <10$ and the battery temperatures are not higher than 15°C while riding and 18°C while charging."

## Sport

- Suspension tuning.
- [Higher speed gearing option](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_6&products_id=181)

## Track

[Hollywood Electrics](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Hollywood_Electrics) has the most experience with racing Zero motorcycles, and often work on request to provide solutions or customize bikes.

**Performance upgrades

- [Higher speed gearing option](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_6&products_id=181)
- [MBB settings](https://web.archive.org/web/2025/https://zeromanual.com/wiki/MBB_Console) (disable upper limits)**

**Cornering**

Remove the kickstand which has an impact on left-hand lean angle.

**Heat Management**

- Motor / controller cooling improvements (IPM might improve this for the motor)
- Removing or taping plastic bits.
- Tire selection.
- [Footpeg relocation](Advanced_Modifications.md#Footpeg_Relocation "Advanced Modifications").
- [Rear brake relocation to left handlebar](Advanced_Modifications.md#Left_Hand_Rear_Brake "Advanced Modifications").
- Disable / remove / do not engage the onboard charger, which heats the battery through the bottom case plate.

**Weight Reduction Checklist**

- Turn signals.
- Belly pan and onboard charger.
- Cosmetic plastics (lower side fairings).

**Fairings**

- Fairings reduce energy consumed and therefore heat build-up.
- Sport fairing fitment.

## Offroad

- [Disable ABS](Common_Modifications.md#Disable_ABS "Common Modifications") for trail braking.
- Suspension tuning.
- [Higher torque gearing option](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_6&products_id=182).
- [FX chain upgrade](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_6&products_id=192).
- [FX rear shock upgrade (Fox)](http://www.zeromotorcycles.com/shop/index.php?main_page=product_info&cPath=15_6&products_id=120)
- Knobby tire selection.
- Upgrades:
  - Handguards
  - Brakes
  - Suspension
  - Spoked wheels

## Offgrid

### Portable Generator Charging

A portable diesel generator with a capacity of about 2kW should be suitable for charging a Zero.

An effective 60mpg has been noted in one case for a full charge (1.5 gallons for a 90 mile range presumably).

**References**

[Charging using portable generators (Tesla but should work with Zero too)](http://electricmotorcycleforum.com/boards/index.php?topic=6612)

[Generator Charging a Tesla? Generac VS Honda](https://www.youtube.com/watch?v=Nf6WgQfL7DY)

## [Travel](Travel.md "Travel")

(moved to its own article)

## Storage

Long-term storage deserves different treatment for a Zero motorcycle than a gas motorcycle, mainly for battery health.

Zero provides [official charging recommendations](http://www.zeromotorcycles.com/owner-resources/charging-recommendations/) for long-term storage (defined as greater than 30 days):

- Discharge to 60% before leaving unattended.
- Check SoC at least monthly.
- Charge it back up to 60% if it drops below 30%.
- Charge it for 24 hours before taking it for a ride to ensure optimal cell balance.

**Video Guide**

[How to Store an Electric Motorcycle Long-Term](https://www.youtube.com/watch?v=SmhHRyhEtc4) by NewZeroLand on YouTube

### Storage Priorities

1. Maintain the battery within its recommended temperature range (not below freezing or too hot - see [Zero's Hot and Cold Weather Operations Guide](http://www.zeromotorcycles.com/owner-resources/Cold-and-Hot-Weather-Operation.pdf)).
2. Leave the battery at a relatively high SoC (60-80% ideal; 70% official; 100% is acceptable).
3. Check the state of charge and system health at least once a month.
4. Perform a charge and full cell rebalancing if the state of charge is too low (40% say; 30% official).

### Plugged-in Storage

**Procedure**

1. Plug the bike in and walk away.
2. Check on the bike monthly for charging failures or other discrepancies.

**Advantages**

- This works completely unattended.
- This tends to keep the battery warm if stored in an unheated space over the winter.
- Cel balance is more or less ensured in the long term.
- It's historically OEM-recommended.

**Disadvantages**

- *If left topped-off for more than a few days*, the battery will age slightly faster (but not faster than the OEM claims) not being nearer the middle of its charge band (40-60%).
- *If left topped-off for more than a few days*, the BMS will be cycling repeatedly over time, which exposes it to more chances of operational glitches or failures while unattended.
- **Note:** 100% SoC indicated is not peak chemical voltage, so the cell stress isn't the same as for small packs or individual consumer cells.

**Note**

This OEM recommendation started when Zero batteries were much smaller, and the largest battery capacities currently sold have a much larger margin of safety around the discharge rate and so can be leaved unplugged with an occasional maintenance visit.

### Unplugged Storage

**Procedure**

1. Perform a cel balance (charging to 100% and leave on a charge until the app reports cel balance of a small number of mV).
2. Ride the bike until voltage is in the 60-80% range (70% official).
3. Leave unplugged unattended and schedule times to check on it periodically.
4. When checking, if SoC is below 40% (30% official), repeat the procedure.

**Advantages**

- The battery will age more slowly.
- *Recently* also OEM-recommended for long-term storage.

**Disadvantages**

- This requires attending to the bike on a (1 month, say) schedule to recharge it until cel balancing is restored fully, and then riding it and putting it back in unplugged storage.

### Storage Theory

**Background**

A Zero motorcycle doesn't contain any fluids that age poorly like gasoline or oil.

Obviously, Zero motorcycles *do* have a giant lithium battery, and they could present a possibility of danger if they drift into a bad state while unattended.

Even while unplugged, the Zero BMS is constantly powered by the battery and draws a tiny amount of power to monitor the battery.

However, the BMS does *not* actively maintain cel balance unless plugged in to an external power source in charging mode.

Generally refer to the [Battery article](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Battery)

**Charge State**

Ideally, keep the battery charged in the 40-60% range as near as practical (to maximize lifetime chemistry).

If left off the charger, the battery will discharge very gradually on its own over (perhaps) several months or years, from the BMS load.

The BMS alone doesn't draw much power at all, under a watt, but to be safe (because slow electrical loads can arise without symptoms), check on the bike.

Schedule an occasional charge period to balance cell voltages, and then restore the charge to the middle of the range for chemistry maintenance.

**Estimating discharge rate**

The BMS continuous power draw has been estimated at 150mA which would use 3.6Wh per day, pretty small.

At this rate, an 11.4kWh battery would discharge completely over ten years, but a 2.8kWh FX/FXS brick would discharge in two years.

*In principle*, this means you can walk away from your bike unplugged and not worry about it.

*Realistically*, you should check on the bike monthly in case this assumption is wrong or the bike has some kind of very slow load variance not visible over short periods of time.

**Temperature**

Not too hot or cold

See [Zero's Hot and Cold Weather Operations Guide](http://www.zeromotorcycles.com/owner-resources/Cold-and-Hot-Weather-Operation.pdf) for specific limits.

**Tires**

Check and maintain tire pressure once a month.

Move the bike on occasion to minimize tire patch wear-in, or just lift the bike on a stand.

**Long-term maintenance cycles**

Brake fluid and eventually tire and cable brittleness.

**Discussions references**

[Balance Voltage in Storage](http://electricmotorcycleforum.com/boards/index.php?topic=6581.0)

[Change to Charging - Leaving Bike Plugged In](http://electricmotorcycleforum.com/boards/index.php?topic=6707.0)

