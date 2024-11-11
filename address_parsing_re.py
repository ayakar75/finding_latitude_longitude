import re


def parse_address(address):
    # Adres parse işlemi için virgülün zorunlu olmadığı bir regex deseni
    pattern = r"(?P<sokak>[\w\s]+ (Sokak|Cadde|Bulvar))\s*(,?\s*)?(?P<mahalle>[\w\s]+ Mahalle)?\s*(,?\s*)?(?P<ilce>[\w\s]+ İlçesi)?\s*(,?\s*)?(?P<sehir>[\w\s]+)?"
    match = re.search(pattern, address)

    if match:
        return {k: v for k, v in match.groupdict().items() if v is not None}
    else:
        return "Adres formatı tanınamadı, lütfen farklı bir adres deneyin."


# Örnek adres girişleri
address1 = "Atatürk Bulvarı, Çankaya Mahallesi, Çankaya İlçesi, Ankara"
address2 = "Atatürk Bulvarı Çankaya Mahallesi Çankaya İlçesi Ankara"
address3 = "Atatürk Bulvarı Ankara"

parsed_address1 = parse_address(address1)
parsed_address2 = parse_address(address2)
parsed_address3 = parse_address(address3)

print("Adres Bileşenleri (1):")
print(parsed_address1)
print("\nAdres Bileşenleri (2):")
print(parsed_address2)
print("\nAdres Bileşenleri (3):")
print(parsed_address3)
