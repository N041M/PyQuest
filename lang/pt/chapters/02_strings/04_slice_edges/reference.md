Os limites de uma fatia podem ser **negativos**, contando a partir do fim, e os dois estilos
combinam-se livremente. `s[1:-1]` elimina o primeiro e o último caractere — começa no
índice 1, para mesmo antes do último.

- Uma fatia cujo início esteja no ou para lá do seu fim é **vazia**, não um erro:
  `s[3:3]` e `s[5:2]` dão ambos `""`.
- Os limites fora do intervalo são ajustados, por isso o fatiamento é tolerante onde a
  indexação simples gera erro: `s[1:99]` está bem.
- Como o `stop` é exclusivo, `s[:-1]` remove exatamente o último caractere e
  `s[1:]` remove o primeiro.

```python
s = "Python"
s[1:-1]   # 'ytho'  -- both ends trimmed
s[2:2]    # ''      -- empty, not an error
```
