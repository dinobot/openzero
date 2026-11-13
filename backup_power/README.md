# Backup power — the pack as a household / camping energy source

Researched 2026-11-05 (owner brainstorm). Nothing bought, nothing wired. This records what is
realistic, what it costs in range, how to connect, and what not to do. Numbers: 30S Gotion LFP,
5.0 kWh nominal, 52 A cell ceiling (≈ 5 kW), ~55 Wh/km measured mixed consumption.

## The one rule

The pack is a 5 kWh power station (an EcoFlow Delta Pro is 3.6 kWh). Power is not the limit: 52 A at
96 V is 5 kW, more than one household circuit. The limit is range: **every 1 kWh spent at the camp is
18 km less ride home.** Usable camp energy = 5 kWh − 55 Wh/km × distance home − ~0.5 kWh reserve.

## How to take energy out

Nothing runs on 96 V directly; one of three converters is needed.

| Path | Hardware | Use |
|---|---|---|
| Inverter 96 V DC → 120 V AC | 96 V is a standard tier of Chinese off-grid inverters (12/24/48/96 V), pure sine 1–5 kW, $150–400. Or two-stage: 96 → 48 V DC-DC + a brand 48 V inverter (Victron etc.) | Everything with a mains plug |
| Buck 72–120 V → 12 V, 20–30 A | Golf-cart / e-moto modules, 250–360 W, $20–40. Take an **isolated** one so B− is not tied to other equipment's chassis. Leave the bike's own Sevcon 622-11202 alone (sized for the lights) | All "12 V camping" gear: compressor fridge, lights, USB-C PD, Starlink Mini, fan, heated vest |
| No hardware: 96–109 V DC into a "100–240 V" device | Switch-mode supplies (laptop bricks, USB chargers, LED drivers) rectify the input and run on DC | Garage trick only: some bricks drop out below 100 V (empty pack = 87 V); anything with relays, bimetal thermostats, triacs or brushed motors fails or arcs on DC |

Inverter rules: ≤ 3 kW continuous so the surge stays inside the cells' 30 s pulse rating; low-voltage
cut-off set to ~88–90 V, above the ANT discharge cut (84 V); idle draw 10–25 W, never leave it on.

## What is realistic and what it costs in range

| Load | Power | Energy | Range cost |
|---|---|---|---|
| 12 V compressor fridge | ~45 W average | 1.1 kWh/day | 20 km/day |
| Starlink standard / Mini | 60 / 30 W | 1.4 / 0.7 kWh/day | 25 / 13 km |
| Laptop + phones + lights | ~20 W | 0.5 kWh/day | 9 km |
| Electric blanket, one night | 60 W | 0.5 kWh | 9 km |
| Kettle, 1 l | 1.5 kW, 4 min | 0.1 kWh | 2 km |
| Induction hob, 30 min | 1.8 kW (19 A from the pack) | 0.9 kWh | 16 km |
| Microwave, 10 min | 1.5 kW | 0.25 kWh | 5 km |
| Charge a 500 Wh e-bike | | 0.6 kWh | 11 km |
| MMA inverter welder, 1 h of work | 2.5 kW in the arc | ~0.7 kWh | 13 km |
| Fan heater 1.5 kW | | whole pack in 3.3 h | everything |

Fridge + Starlink + gadgets + cooking ≈ 3 kWh/day: one day of camp with 40 km home in reserve.
Resistive space heating is not realistic; spot heating (kettle, blanket, hob) is cheap. Circular saw
and drill use little energy but need an inverter with surge headroom (universal motors draw 2–3× at
start). Curiosity: through a 120 V EVSE at 1.4 kW the pack adds ~20 km to a car, so rescuing a
stranded EV to the next outlet is physically real. As a house UPS, 5 kWh is a fridge + router + lights
for a day.

## Connection point

- **Pack SB50, bike side unplugged** (the same point as road-kit charging, through the ANT and the
  Class T fuse). Unlike charging, the Sevcon does not need isolating for a load. This exists today
  with zero hardware; its only cost is lifting the seat.
- SB50 is rated by Anderson for hot-plugging at 50 A / 120 V DC, so an inverter up to ~2 kW can be
  plugged live, but big inverters have input capacitors: use a precharge resistor in the plug or an
  inverter with soft-start.
- Each load gets its own DC-rated fuse (Class T or MIDI). 100 V DC arcs and does not self-extinguish.
- ANT cuts discharge at −10 °C: a winter camp hits that before it hits capacity.
- Minimal "V2L" build if it is ever wanted: isolated 96 → 12 V / 300 W buck plus a 48 V branch for a
  brand inverter, both from the pack SB50 through their own fuses. Covers the whole table except welding.

## Using the on-bike charge port as a load port

The charge port (SB50 in the stock location) sits behind a series diode and is therefore input-only
(see CLAUDE.md "Charging"). Options, in order of effort:

1. **Do nothing**: use the pack SB50 under the seat (above). The right answer until an inverter exists.
2. **Manual bypass**: a rotary **PV DC isolator** (32 A / 1000 V DC, IP66, $20–40) in parallel with the
   diode. The only cheap switch class that honestly breaks 30 A at 100 V DC; automotive / marine
   battery switches are 48 V parts and will burn on a DC arc. Normally off = port dead; on = port live,
   with a "port live" LED next to it. Fail-safe both ways: charger with bypass on sees the pack as if
   there were no diode; load with bypass off gets nothing. Mount it where it is seen (under the seat)
   so the bike is never ridden with a live port.
3. **Automatic bypass**: a DC contactor across the diode, closed only by a "right plug": magnet in the
   inverter's SB50 housing, reed switch in the bike-side housing (SB50 has no auxiliary contacts; only
   SB120/175 do). The charger's plug has no magnet, so it keeps the diode path. Add a precharge
   resistor across the contactor with ~1 s delay (the Sevcon scheme) so the inverter's capacitors do
   not weld the contacts. J1772-style "live only with a plug inserted", but a project, not an evening.

Do not: remove the diode; "precharge" with a resistor across the diode (100 Ω at 100 V is 1 A out of
an open port, exactly what the diode prevents). Any bypass needs the port lead re-sized (chosen for
18 A charging; a 2–3 kW inverter is 20–30 A) and the port negative on P− through the ANT so its
protections work in the discharge direction too.

## Not realistic, and why

- Solar into the pack at camp: needs an MPPT with ~110 V output; Victron stops at 48 V systems, the
  rest is a rare Chinese niche.
- Sevcon as a grid or AC source: the phase outputs are not a sine into a socket.
- Jump-starting cars from the 12 V rail: the Sevcon DC-DC is sized for lights (slow-charging a car
  battery is fine).
- Heating anything straight from 100 V DC: a 120 V hot plate physically runs at 70 % power, but its
  switch and thermostat are AC parts and weld on DC. Everything that heats lives on 12 V or behind
  the inverter.
