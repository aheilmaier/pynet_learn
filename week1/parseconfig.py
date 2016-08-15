from ciscoconfparse import CiscoConfParse

ipseccfg = CiscoConfParse("../../pynet/pyth_ans_ecourse/class1/cisco_ipsec.txt")

for i in ipseccfg.ConfigObjs:
    print i.text

crypto_maps = ipseccfg.find_objects(r"^crypto map CRYPTO")
for i in crypto_maps:
    print i.text
    for n in i.all_children:
        print n.text

# Find all of the crypto map entries that are using PFS group2
crypto_maps_pfs2 = ipseccfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec="pfs group2")
print "PFS group2 crypto maps:"
for i in crypto_maps_pfs2:
    print i.text

# Find crypto maps not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.
crypto_maps_no_aes = ipseccfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec="transform-set AES")
print "cryptomaps wo aes:"
for i in crypto_maps_no_aes:
    print i.text
    for n in i.all_children:
        if n.text.startswith(" set transform-set"):
            print n.text
