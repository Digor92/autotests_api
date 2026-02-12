from jsonschema import validate


schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  },
  "required": ["name"]
}
data1 = {
    "name":"Alice",
    "age": 30
}
data2 = {
    "name":50,
    #"age": 30
}
validate(instance=data1, schema=schema)
validate(instance=data2, schema=schema)
