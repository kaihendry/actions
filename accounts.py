import random, json

regions = ["eu-west-1", "eu-central-1", "us-east-1"]
envs = ["dev", "int", "uat", "tst", "stg", "prd"]
groups = ["mango", "banana", "apple", "kiwi", "grape"]

rand12 = lambda: str(random.randint(10**11, 10**12 - 1))


mock = {
    g: {
        e: {
            "account": rand12(),
            "description": f"{g} {e} account",
            "region": random.choice(regions),
        }
        # dev always present; add 0–3 random other envs
        for e in ["dev"] + random.sample(envs, random.randint(0, 3))
    }
    for g in groups
}

print(json.dumps(mock, indent=4))
