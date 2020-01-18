dist_AB = float(input())
v_A = float(input())
v_B = float(input())

v_A_km_min = v_A / 60
v_B_km_min = v_B / 60

tempo_min = dist_AB / (v_A_km_min + v_B_km_min)
pos = v_A_km_min * tempo_min

print("%.2f min" % tempo_min)
print("%.2f km" % pos)
