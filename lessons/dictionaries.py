# Initialize dictionary
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# dictionary length
print(len(ice_cream))

# Add to dictionary
ice_cream["mint"] = 10

# Interact with dictionary by key
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# Update value by key
ice_cream["mint"] += 1

# Remove value by key
ice_cream.pop("strawberry")

# Test a key
print("vanilla" in ice_cream)

# For...in... loop
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")

print(ice_cream)

test_list: list[str] = ["un", "deux", "trois"]
print(test_list)
