describe("conversion to roman numerals", function() {
    it("0 to 10", function() {
        expect((1).toRoman()).toEqual("I");
        expect((2).toRoman()).toEqual("II");
        expect((3).toRoman()).toEqual("III");
        expect((4).toRoman()).toEqual("IV");
        expect((5).toRoman()).toEqual("V");
        expect((6).toRoman()).toEqual("VI");
        expect((7).toRoman()).toEqual("VII");
        expect((8).toRoman()).toEqual("VIII");
        expect((9).toRoman()).toEqual("IX");
        expect((10).toRoman()).toEqual("X");
    });

    it("11 to 100", function() {
        expect((11).toRoman()).toEqual("XI");
        expect((22).toRoman()).toEqual("XXII");
        expect((33).toRoman()).toEqual("XXXIII");
        expect((44).toRoman()).toEqual("XLIV");
        expect((50).toRoman()).toEqual("L");
        expect((55).toRoman()).toEqual("LV");
        expect((66).toRoman()).toEqual("LXVI");
        expect((77).toRoman()).toEqual("LXXVII");
        expect((88).toRoman()).toEqual("LXXXVIII");
        expect((99).toRoman()).toEqual("XCIX");
        expect((100).toRoman()).toEqual("C");
    });

    it("101 to 1000", function() {
        expect((111).toRoman()).toEqual("CXI");
        expect((222).toRoman()).toEqual("CCXXII");
        expect((333).toRoman()).toEqual("CCCXXXIII");
        expect((444).toRoman()).toEqual("CDXLIV");
        expect((500).toRoman()).toEqual("D");
        expect((555).toRoman()).toEqual("DLV");
        expect((666).toRoman()).toEqual("DCLXVI");
        expect((777).toRoman()).toEqual("DCCLXXVII");
        expect((888).toRoman()).toEqual("DCCCLXXXVIII");
        expect((999).toRoman()).toEqual("CMXCIX");
        expect((1000).toRoman()).toEqual("M");
    });

    it("greater than 1000", function() {
        expect((1111).toRoman()).toEqual("MCXI");
        expect((2222).toRoman()).toEqual("MMCCXXII");
        expect((3333).toRoman()).toEqual("MMMCCCXXXIII");
        expect((3888).toRoman()).toEqual("MMMDCCCLXXXVIII");
        expect((3999).toRoman()).toEqual("MMMCMXCIX");
    });
});

