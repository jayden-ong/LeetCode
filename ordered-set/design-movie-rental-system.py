class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.free = {}
        self.rented = SortedList()
        self.shop_movie_to_price = {}
        for shop, movie, price in entries:
            self.shop_movie_to_price[(shop, movie)] = price
            if movie not in self.free:
                self.free[movie] = SortedList()
            self.free[movie].add((price, shop))

    def search(self, movie: int) -> List[int]:
        answer = []
        if movie not in self.free:
            return []
        
        for (price, shop) in self.free[movie]:
            answer.append(shop)
            if len(answer) == 5:
                return answer
        return answer

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[(shop, movie)]
        self.free[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_to_price[(shop, movie)]
        self.free[movie].add((price, shop))
        self.rented.remove((price, shop, movie))

    def report(self) -> List[List[int]]:
        answer = []
        for (_, shop, movie) in self.rented:
            answer.append((shop, movie))
            if len(answer) == 5:
                break
        return answer

        


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()