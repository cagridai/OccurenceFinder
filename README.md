## Proje Açıklaması

- Verilen `t` dizisindeki tüm alt diziler bulunur ve her alt dizi için `z` dizisinde kaç kez tekrarlandığı hesaplanır. Sonuç olarak, her bir alt dizinin uzunluğu ile tekrar sayısının çarpımı alınır ve bu değerlerden en büyüğü döndürülür.

## Kullanım
- main.py'nin bulunduğu dizinde terminale "python3 main.py" komutu yazılarak çalıştırılır

### Örnek Kullanım

```python
t = "acldm1labcdhsnd"
z = "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"
print(find_max(t, z))  # Çıktı: 20