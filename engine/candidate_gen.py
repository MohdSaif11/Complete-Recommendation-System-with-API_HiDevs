class CandidateGenerator:

    def __init__(self, user_data, item_data):
        self.user_data = user_data
        self.item_data = item_data

    def collaborative_candidates(self, user_id, limit=20):
        if user_id not in self.user_data:
            return []

        user_items = set(self.user_data[user_id])
        candidates = set()

        for other_user, items in self.user_data.items():
            if other_user == user_id:
                continue

            if user_items & set(items):
                candidates.update(items)

        # remove already seen items
        candidates -= user_items

        return list(candidates)[:limit]

    def popularity_candidates(self, limit=20):
        popularity = sorted(
            self.item_data.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )
        return [item for item, _ in popularity[:limit]]

    def hybrid_candidates(self, user_id, limit=20):
        user_items = set(self.user_data.get(user_id, []))

        collab = self.collaborative_candidates(user_id, limit)
        popular = self.popularity_candidates(limit)

        combined = set(collab + popular)

        # strict filtering
        filtered = [item for item in combined if item not in user_items]

        return filtered[:limit]