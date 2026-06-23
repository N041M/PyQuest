# 4.2 -- Změna seznamu

## Koncept

Na rozdíl od řetězců lze seznamy **měnit na místě** (jsou *měnitelné*). Několik
způsobů:

- Nahradit položku podle indexu: `nums[0] = 99`
- Odebrat a vrátit **poslední** položku: `nums.pop()`
- Odebrat první odpovídající **hodnotu**: `nums.remove(20)`

```python
nums = [10, 20, 30]
nums[0] = 99      # [99, 20, 30]   replace by position
nums.pop()        # [99, 20]       drop the last item (returns 30)
print(nums)       # [99, 20]
```

Tyto mění existující seznam -- proměnná stále ukazuje na tentýž seznam, nyní
pozměněný.

## Příklad

```python
xs = [1, 2, 3]
xs[1] = 0
xs.pop()
print(xs)         # [1, 0]
```

## Tvůj úkol

Přečti počet `n` (alespoň 1), pak `n` čísel, do seznamu. Pak:

1. **zdvojnásob první položku** (nahraď `nums[0]` hodnotou `nums[0] * 2`) a
2. **odeber poslední položku** pomocí `.pop()`.

Vypiš výsledný seznam. Pro vstup `3`, pak `5`, `2`, `9`:

```
[10, 2]
```

(`[5, 2, 9]` -> zdvojnásob první -> `[10, 2, 9]` -> pop -> `[10, 2]`.)

## Hotovo, když

- `5, 2, 9` dá `[10, 2]`.
- Jediné číslo `n=1` (např. jen `4`) dá `[]` -- zdvojnásobeno na `[8]`, pak je
  poslední (jediná) položka odebrána.
