def main():
  specifications = {"name": "James Webb Telescope"}
  specifications.update({"distance": 0.01, "orbit": "sun"})
  print(create_report(specifications))

def create_report(spacecraft):
  return f"""
  ========REPORT========

  NAME: {spacecraft.get("name", "Unknown")}
  DISTANCE: {spacecraft.get("distance", "Unknown")} AU
  ORBIT: {spacecraft.get("orbit", "Unknown")}

  ======================
  
  """

main()