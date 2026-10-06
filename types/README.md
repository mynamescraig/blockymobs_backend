# Types - a brief explanation:
the types appear in a large "types" dict like so:

### Sample Types JSON
```json
{
  "types": {
    "water": {
      "fire": -1
    }
  }
}
```
Every type falls into the `"types":` dict.

They should appear with their name, in this case `"water"`, alongside it's own separate dict. Within the dict you can see `"fire": -1`, in this case the integers represent effectiveness.

-1 is the modifier applied to damaging moves when using the specified (`"fire"`) type against the original (`"water"`) type. Each dict only shows how another type affects the original (so how effective fire is against water types in this case.)

This is to avoid a huge duplication issue my previous iteration had!

### This should go without saying, but we will write it anyway

DO NOT duplicate types! There is only one water type. There only ever can be one water type. This will break the flow if you try duplicating types.