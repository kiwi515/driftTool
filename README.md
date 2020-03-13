# driftTool
The days of changing each REFF color value manually are over. (They probably were a while ago but no one told me)  
</br>
This tool works with any RKRace.breff file, regardless of its file size, as everything is calculated rather than only using static offsets. Just extract one from a Common.szs, run it through the script, and insert the outputted BREFF.

`driftTool.py RKRace.breff primaryColor secondaryColor`  
</br>
Colors must **not** include alpha values. This is because Mario Kart Wii uses multiple alpha values throughout its many drift effects, as such, this script keeps the vanilla alpha values

## Supported Features:
- [X] Support bike drifts (blue drift/mini-turbo)
- [ ] Remove color animations on a few effects
- [ ] Support kart drifts (orange drift/super mini-turbo)
