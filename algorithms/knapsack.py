
def knapsack(parcels, capacity):

    n = len(parcels)
    dp = [[0 for x in range(capacity + 1)]
          for x in range(n + 1)]

    for i in range(1, n + 1):

        weight = int(parcels[i - 1]["weight"])
        value = int(parcels[i - 1]["value"])

        for w in range(capacity + 1):

            if weight <= w:

                dp[i][w] = max(
                    dp[i - 1][w],
                    value + dp[i - 1][w - weight]
                )

            else:

                dp[i][w] = dp[i - 1][w]

    selected_parcels = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected_parcels.append(parcels[i - 1])

            w -= int(parcels[i - 1]["weight"])

    selected_parcels.reverse()

    return selected_parcels, dp[n][capacity]

if __name__ == "__main__":

    parcels = [
        {"parcel_id": "P101", "weight": "5", "value": "500"},
        {"parcel_id": "P102", "weight": "8", "value": "650"},
        {"parcel_id": "P103", "weight": "4", "value": "450"},
        {"parcel_id": "P104", "weight": "10", "value": "700"},
        {"parcel_id": "P105", "weight": "6", "value": "550"}
    ]

    capacity = 25

    selected, total_value = knapsack(parcels, capacity)

    print("Selected Parcels:")

    total_weight = 0

    for parcel in selected:
        print(parcel["parcel_id"],
              "Weight:", parcel["weight"],
              "Value:", parcel["value"])

        total_weight += int(parcel["weight"])

    print("\nTotal Weight:", total_weight, "kg")
    print("Total Value:", total_value)
