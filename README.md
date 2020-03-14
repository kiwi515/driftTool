# driftTool
The days of changing each REFF colour value manually are over. (They probably were a while ago but no one told me)  
</br>
This tool works with any RKRace.breff file, regardless of its file size, as everything is calculated rather than only using static offsets. Just extract one from a Common.szs, run it through the script, and insert the outputted BREFF back into your Common.szs.

`driftTool.py RKRace.breff primaryColour secondaryColour`  
</br>
Colours must **not** include alpha values. This is because Mario Kart Wii uses multiple alpha values throughout its many drift effects, as such, _this script keeps the vanilla alpha values._ For now, _leave hash-tag prefixes out of the hex colours as well,_ I haven't gotten around to implementing those yet.

## Supported Features:
- [X] Support bike drifts (blue drift/mini-turbo)
- [ ] Remove colour animations on a few effects
- [ ] Support kart drifts (orange drift/super mini-turbo)
- [ ] Support editing Common.szs rather than extracting/replacing RKRace.breff
- [ ] Allow for the "mini-turbo" (engine boost) colours to automatically match the drift (optional for the user)

### Feel free to contact me on Discord if you have any issues. kiwi#5018
