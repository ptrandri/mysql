s = 'faaf0014001b86392103724513400063db0d010060ac640fb1441f801c82020924d3f2ea78b6d4b49842153804bd1c2704bfc688bdaa84c6029d89af24d3f2ea7b4aaf44fb5a3bcf3cae98f4280356b8ad2c957f228210a94413d0262366a900000003421a66660000000040d10a40000000000000faaf'
result = ' '.join(s[i:i+2] for i in range(0, len(s), 2))
print(result)
