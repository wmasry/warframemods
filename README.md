# warframemods
Script to pull warframe mod info 'full or partial name' or all mods

```
$ python mod.py wildfire

Name: Wildfire
Polarity: Madurai
Rarity: Rare
Description: +5% Magazine Capacity,+15% <DT_FIRE>Heat
```

Partial Name
```
$ python mod.py hallowed

Name: Hallowed Eruption
Polarity: Zenurik
Rarity: Rare
Description: Hallowed Ground Augment: The next time this ability is cast it will consume the Hallowed Ground, dealing the remaining damage in a burst with 30% Proc Chance of <DT_RADIATION>Radiation.


Name: Hallowed Reckoning
Polarity: Zenurik
Rarity: Rare
Description: Reckoning Augment: Enemies affected by Reckoning spawn zones that increase Armor by 150 for allies and inflicts 100 Damage to enemies over 7s.
```
Pull all mods
```
$ python mod.py ""
```
Show raw data for mod
```
$ python mod.py wildfire all

Name: Wildfire
Polarity: Madurai
Rarity: Rare
Description: +5% Magazine Capacity,+15% <DT_FIRE>Heat


{u'polarity': u'Madurai', u'category': u'Mods', u'name': u'Wildfire', u'fusionLimit': 3, u'rarity': u'Rare', u'tradable': True, u'imageName': u'wildfire.jpeg', u'uniqueName': u'/Lotus/Upgrades/Mods/Rifle/DualStat/WildfireMod', u'baseDrain': 6, u'drops': [{u'chance': 0.18969999999999998, u'type': u'Transient Rewards', u'location': u'Nightmare Mode Rewards', u'rarity': u'Uncommon'}], u'type': u'Rifle', u'patchlogs': [{u'name': u'Recurring Nightmares', u'url': u'https://forums.warframe.com/topic/711418-recurring-nightmares/', u'fixes': u'', u'date': u'2016-10-27T19:03:48Z', u'additions': u'', u'changes': u'Wildfire', u'imgUrl': u'http://i.imgur.com/Oail8jd.jpg'}], u'description': u'+5% Magazine Capacity,+15% <DT_FIRE>Heat'}
```
