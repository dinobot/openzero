---
title: "Working with Zero"
source: https://zeromanual.com/wiki/Working_with_Zero
archived: https://web.archive.org/web/20250312183254/https://zeromanual.com/wiki/Working_with_Zero
captured: 2025-03-12
last_modified: "4 June 2019 21:32"
categories: ["Manufacturer"]
---

# Working with Zero

This helps navigate how to work with Zero Motorcycles from a customer perspective.

## Dealership Model

Zero has a customer service hotline and an email alias for receiving bike logs for diagnosis, but will generally refer all non-trivial interactions to a local dealer.

## Escalating customer support issues

In case you encounter a quality issue with your Zero Motorcycles, here is the typical escalating process to follow:

1. Talk to the dealer who sold you the motorbike.

   In many cases issues (see the recalls list[[[1]](Recalls.md)]) are documented or can be dealt with in the context of the commercial warranty.

   If you encounter a problem after the commercial warranty is over, it can still be fixed if it is a [latent defect](https://en.wikipedia.org/wiki/Latent_defect) or a [hidden defect](https://www.europe-consommateurs.eu/en/consumer-topics/buying-goods-services/guarantees-warranties/guarantees-warranties-in-france/hidden-defects/).

   For this, you will need to prove that it is indeed a defect by collecting proofs (expertise, pictures, videos, testimonies,...).
2. If the dealer refuses to solve the issue because it stopped supporting Zero Motorcycles, you'll need to contact another dealer

   Use [Zero's dealers locator](https://www.zeromotorcycles.com/locator/) to locate one close to you.
3. If you think the problem is not related with anything you did (fall, bad handling,...) and if this is an issue you can solve yourself, start with Zero's Unofficial Manual [[2]].

   You can also look at user forums such as [Electric motorcycles forum](http://electricmotorcycleforum.com) for solutions.
4. In case the problem is too complex / expensive and you still think it is on Zeromotorcycles' side, you can contact them through twitter [ZeroMotorcycles' twitter account](https://twitter.com/ZeroMC) or through their customer support [Zero Customer Support](mailto:support@zeromotorcycles.com).

   Be aware that Zero Motorcycles is a very small company with very limited resources - so make you message short and clear about the issue, its consequences and why you think ZeroMotorcycles should solve it.
5. If you do not get a satisfactory answer, then you'll need to consider a legal action.

   A first step for this can be to ask your insurance for legal support (if you contract allows it, they will cover the cost of the expertise as well as the legal expenses).
6. If all the other options fail, then you will need to hire a lawyer and to sue the dealer who sold you the bike (then, the dealer himself can sue ZeroMotorcycles if you win) - in most cases you cant sue directly ZeroMotorcycles (or its representative in you country), unless you start a [class action](https://en.wikipedia.org/wiki/Class_action) with several users sharing a similar case.

While this process might be really irritating, you will raise your chances of reaching an acceptable solution by staying calm, factual and sharing the issues you encountered as well as the solutions you found with the user community.

## [Ordering Parts](https://web.archive.org/web/2025/https://zeromanual.com/wiki/Ordering_Parts)

Zero provides dealers software for ordering parts.

The parts program is run over the Web, probably from Zero HQ.

It's similar to mainstream motorcycle manufacturer software, but not identical - and at least one difference can significantly affect ordering (see below).

The standard parts-ordering model is to have the parts sent to the dealer, where they can be picked up or re-shipped to the customer.

This lets the dealer handle issues, but offers a point of delay if communication between the dealer and Zero is not regular.

Ordering through a dealer for shipping directly to the customer may be more expedient

**Interaction**

- There's a main drop-down menu set that shows the various Zero models and years.
- The user specifies a year and model, orders parts for it, then changes to a different year and/or model to order parts for that one.

  The fleet models (DSP, MMX, etc.) have not been noticed in this selector.
- Once the model & year are selected, there are various diagrams that can be opened.
- The user clicks on a number in the diagram, and a new window opens with specific part information.

  There's no parts list underneath corresponding to the diagram numbers.
- Part information is a single line listing:
  1. Part number
  2. Brief Descriptive Name
  3. (Occasional) long description
  4. Price
- All this info (including superseding P/N's) is included on other ordering programs' parts lists, under the diagrams.

**Parts Listed As Not Available**

One thing you do *not* want to see in the part screen is **Part Not Available** (which seems to mean **Part Availability not available**).

Workarounds:

- Re-ordering the parts in the next order seems to work consistently despite this.
- If the part you want is used over several models and/or years, you could potentially order the same part for multiple years/models, and chances are one of them will show as available and can actually be ordered.

Since all this parts stuff is dealer-eyes-only it's pretty difficult to determine for certain which parts are used for which years - Zero website photos are one guide.

An interesting hint: regarding the chain kit, all the individual parts can be ordered from the '13 MX section, along with the shock protector.

**Parts Revisions**

Zero doesn't really supercede parts numbers in the Honda sense (giving new part numbers to identical or nearly-identical older parts, usually when they're used again on a later-model machine and/or are supplied by a new vendor).

Instead, Zero does part substitutions as:

- An older p/n is replaced with the p/n of the latest version of a part with similar function; then the original part number may or may not be removed from the database, resulting in some perfectly-good p/n's for unique older parts that come back as NG when entered. This has happened to me 5 times, resulting in the return of four useless-to-me parts (I would've returned all 5, but I didn't notice the small differences until much later :( ). A 6"-too-long rear brake line is pretty much a joke, completely-different LH frame brackets don't work too well on the RH side, etc. etc.

| Prefix | Meaning |
| --- | --- |
| 00- | Recall |
| 10- | Accessories |
| 11- | Apparel |
| 12- | Dealer Tools |
| 20- | Fasteners / Springs / Wiring Support / Swingarm |
| 21- | Swingarm |
| 22- | Forks / Steering |
| 23- | Wheels |
| 24- | Bodywork |
| 25- | Brakes |
| 26- | Frame |
| 27- | Controls |
| 30- | Final Drive |
| 40- | Boards / Dash / Charger |
| 45- | Contactor / Charger / Headlamp / Controls / Fuses |
| 46- | Battery / Chargetank |
| 56- | Electrical |
| 60- | Controller |
| 65- | Lighting |
| 80- | Logos / Emblems |
| 84- | Transport |
| 86- | Tools |
| 88- | Documentation |
| 90- | Fasteners |

**Reference**

[Zero parts ordering (thread)](http://electricmotorcycleforum.com/boards/index.php?topic=5474)

[Exploded Parts Views](Exploded_Views.md "Exploded Views") tracking page

## Troubleshooting

Zero has a limited sized team which helps dealers troubleshoot electronics systems issues on their bikes with the dealers (125 count claimed publicly).

The dealership will have a Zero-provisioned laptop with OEM software on Windows and a cable harness for connecting to the bike's systems.

The dealership should be (and usually is) comfortable obtaining logs, checking on firmware revisions and upgrading the firmware.

Zero uses remote-control software (LogMeIn Rescue Lens) to drive the software, and can escalate to other technicians or specialists during a session/call.

Many dealers seem to do nothing but wait for an available remote connection time slot to reserve with the manufacturer before proceeding.

Training and support seem to be explicit goals in the remoting feature; hopefully that will become evident.

Perhaps the best a customer can do is encourage their dealer to take advantage of all of this.

**References**

[LogMeIn Rescue for Zero Motorcycles](https://www.themanufacturer.com/articles/logmein-to-the-rescue-for-zero-motorcycles/)

