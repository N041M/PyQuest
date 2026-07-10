Um `except` deve indicar a exceção **específica** que esperas. Apanhar
exatamente o tipo certo permite que erros inesperados apareçam como bugs em
vez de serem silenciosamente engolidos.

- `except ValueError:` apanha apenas esse tipo; uma falha não relacionada
  (um nome mal escrito que levanta `NameError`) continua a propagar-se, o que
  é o que queres.
- Um `except:` sem nome (ou `except Exception:`) apanha **tudo**, incluindo
  bugs que preferirias ver — evita-o a menos que queiras mesmo dizer
  "qualquer falha".
- Faz corresponder o tipo à operação: `int()` levanta `ValueError`, indexar
  levanta `IndexError`, uma pesquisa num dicionário levanta `KeyError`.

```python
try:
    value = data[key]
except KeyError:         # only a missing key, not other bugs
    value = None
```
