dist_AB = float(input())
v_A = float(input())
v_B = float(input())
ponto_D = float(input())
compB = float(input())

v_A_km_min = v_A / 60
v_B_km_min = v_B / 60

tempo_AD = ponto_D / v_A_km_min

print("%.2f min" % tempo_AD)

dist_BD = dist_AB - ponto_D
tempo_BD = dist_BD / v_B_km_min
tempo_comp = (compB / 1000) / v_B_km_min
tempo_B_total = tempo_BD + tempo_comp

print(tempo_AD < tempo_B_total)
