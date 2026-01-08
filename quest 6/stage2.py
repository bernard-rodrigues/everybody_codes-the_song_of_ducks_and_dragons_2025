data = "ABCBCbACCbCcCbbACacaBCbbBcBAAACcAcCAcBBCaaAbACcbccAabABABAaBABAAAAAaacbabbcbCCAaacCAAaaBCbCCbbaBcacaaCcCCABacAbbbacbaacABcAAaABACACccaaBaBBcaAABbAacbBbccCbCBBcaCBACCBAAAbcCacaAAcCcbaAbCabaCCACCBbAAACBaaCCBcabBCAcBCbABbACaCABBbBcCbaAcbcacAAcCaACcaaAbBccacbAaBbaCaABACBbbbCABaBBbCBbABccACCAcaAAbCCaCcbc"

masters = "ABC"
total = 0

for i in range(len(data)):
    if data[i] in masters:
        total += data[i:].count(data[i].lower())

# Output must be 3870
print(total)