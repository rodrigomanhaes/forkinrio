describe("tabuada", function() {
    it("n from 0 to 10", function() {
        expect((5).tabuada()).toEqual([
            "5 x 0 = 0",
            "5 x 1 = 5",
            "5 x 2 = 10",
            "5 x 3 = 15",
            "5 x 4 = 20",
            "5 x 5 = 25",
            "5 x 6 = 30",
            "5 x 7 = 35",
            "5 x 8 = 40",
            "5 x 9 = 45",
            "5 x 10 = 50"
        ]);
    });

    it("specifying begin and end", function() {
        expect((4).tabuada(3, 7)).toEqual([
            "4 x 3 = 12",
            "4 x 4 = 16",
            "4 x 5 = 20",
            "4 x 6 = 24",
            "4 x 7 = 28"
        ]);
    });
});

