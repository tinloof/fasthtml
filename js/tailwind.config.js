/** @type {import('tailwindcss').Config} */
tailwind.config = {
  theme: {
    screens: {
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1440px",
    },
    extend: {
      keyframes: {
        "positive-bounce": {
          "0%": {
            transform: "rotate(4deg)",
          },
          "33%": {
            transform: "rotate(3deg)",
          },
          "66%": {
            transform: "rotate(5deg)",
          },
          "100%": {
            transform: "rotate(4deg)",
          },
        },
        "positive-unbounce": {
          "0%": {
            transform: "rotate(4deg)",
          },
          "100%": {
            transform: "rotate(0deg)",
          },
        },
        "negative-bounce": {
          "0%": {
            transform: "rotate(-4deg)",
          },
          "33%": {
            transform: "rotate(-3deg)",
          },
          "66%": {
            transform: "rotate(-5deg)",
          },
          "100%": {
            transform: "rotate(-4deg)",
          },
        },
        "negative-unbounce": {
          "0%": {
            transform: "rotate(-4deg)",
          },
          "100%": {
            transform: "rotate(0deg)",
          },
        },
      },
      animation: {
        "positive-bounce": "positive-bounce  0.6s ease-in-out forwards",
        "positive-unbounce": "positive-unbounce  0.2s ease-in-out forwards",
        "negative-bounce": "negative-bounce  0.6s ease-in-out forwards",
        "negative-unbounce": "negative-unbounce  0.2s ease-in-out forwards",
      },
      fontFamily: {
        geist: ["Geist", "sans-serif"],
        "geist-mono": ["Geist Mono", "monospace"],
      },
      colors: {
        brown: "#6B2E2E",
        "soft-brown": "#fcc",
        green: "#3CDD8C",
        "soft-green": "#D4F7E6",
        yellow: "#FFC435",
        "soft-yellow": "#fec",
        grey: "#F3F3F3",
        "soft-grey": "#fff",
        pink: "#E699D9",
        "soft-pink": "#FFCCF7",
        purple: "#3A2234",
        "soft-purple": "#EDDEE9",
        blue: "#7575F0",
        "soft-blue": "#E8E8FC",
      },
    },
  },
};
