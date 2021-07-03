# @TODO: Your code here

info = {"name": "Daniel",
        "age":28,
        "hobbies":["golf","eat"],
        "wake":{"monday":5,"sunday":9}}


print(f"My name is {info['name']} and I am {info['age']} years old\n"
      f"I have {len(info['hobbies'])} hobbies\n"
      f"I wake up at {info['wake']['sunday']} on Sundays")
