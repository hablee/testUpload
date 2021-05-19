# locs = [[1345, 801, 1437, 912, 'a'], [1444, 804, 1535, 913, 'b'], [895, 890, 989, 999, 'c'], [1593, 885, 1687, 1000, 'd'], [946, 974, 1038, 1082, 'e'], [1493, 888, 1588, 999, 'f'], [1296, 885, 1388, 998, 'g'], [1393, 888, 1489, 999, 'h'], [1043, 974, 1140, 1085, 'i'], [1225, 541, 1359, 690, 'j'], [1245, 799, 1337, 910, 'k'], [1191, 1260, 1291, 1369, 'l'], [944, 803, 1040, 909, 'm'], [1068, 569, 1188, 705, 'n'], [1045, 801, 1138, 910, 'o'], [1195, 1060, 1289, 1170, 'p'], [1302, 1259, 1394, 1370, 'q'], [996, 1059, 1091, 1174, 'r'], [1145, 799, 1235, 909, 's'], [1294, 1158, 1390, 1270, 't'], [1595, 1061, 1687, 1170, 'u']]
locs = [[1420, 720, 1522, 842, 'a'], [1570, 1166, 1675, 1284, 'b'], [1406, 829, 1503, 950, 'c'], [1383, 1152, 1485, 1271, 'd'], [1504, 784, 1600, 901, 'e'], [1460, 1319, 1573, 1436, 'f'], [1563, 1272, 1665, 1392, 'g'], [1658, 1226, 1764, 1343, 'h'], [1390, 1045, 1490, 1162, 'i'], [1371, 1266, 1477, 1382, 'j'], [1111, 901, 1263, 1056, 'k'], [1508, 679, 1605, 794, 'l'], [1400, 934, 1500, 1055, 'm'], [1670, 1015, 1779, 1135, 'n'], [1499, 888, 1600, 1005, 'o'], [1890, 1038, 1989, 1148, 'p'], [1895, 918, 2003, 1043, 'q'], [1795, 915, 1900, 1038, 'r'], [1702, 582, 1809, 702, 's'], [1517, 570, 1624, 690, 't'], [1134, 1086, 1274, 1227, 'u']]

# for item in locs:
#     print(item[0])

with open("testloc2.txt","w") as f:
    for item in locs:
        strloc = str(item[0])+','+str(item[1])+','+ str(item[2])+','+ str(item[3])+','+ str(item[4])
        f.write(strloc+"\n")  # 自带文件关闭功能，不需要再写f.close()

