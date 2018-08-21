city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
input_city = input('Type the name of the city you want to visit out of, Boston, New York, Albany, Portland or Philadelphia: ')
one_hop = city_to_accessible_cities[input_city]
print(f'Cities that are directly connected to {input_city} are: {one_hop}')
print(f'Cities that can be reached from these cities and are two hops away from {input_city} are:')
while len(one_hop) > 0:
  two_hops = one_hop.pop()
  print(city_to_accessible_cities[two_hops], end=' ')