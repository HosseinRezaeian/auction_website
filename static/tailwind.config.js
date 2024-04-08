/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./dist/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        DanaFaNumThin: "DanaFaNumThin",
        DanaFaNumRegular: "DanaFaNumRegular",
        DanaFaNumMedium: "DanaFaNumMedium",
        DanaFaNumDemiBold: "DanaFaNumDemiBold",
        DanaFaNumBold: "DanaFaNumBold",
        DanaFaNumBlack: "DanaFaNumBlack",
      },
    },
  },
  plugins: [
    function ({ addVariant }) {
      addVariant("child", "&>*");
      addVariant("childhover", "&>*:hover");
    },
  ]
};
