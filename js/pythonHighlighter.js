hljs.registerLanguage("python-custom", (hljs) => {
  var python = hljs.getLanguage("python");

  python.name = "Python Custom";

  python.contains.push({
    className: "decorator",
    begin: "/@/",
    end: "/$/",
    contains: [
      {
        className: "symbol",
        match: "@",
      },
      {
        className: "name",
        begin: /[\w\.]+/,
      },
      {
        className: "params",
        begin: /\(/,
        end: /\)/,
      },
    ],
  });

  var yellowTokens = {
    className: "yellow-char",
    begin: /\*/,
  };
  var whiteTokens = {
    className: "white-char",
    begin: /[,.:()@]/,
  };
  var attributeTokens = {
    className: "attribute",
    begin: /\./,
    end: /[\w]+/,
    contains: [
      {
        begin: /\w+/,
        className: "attr-name",
      },
    ],
  };

  // Remove id from built-in keywords
  python.keywords.built_in = python.keywords.built_in.filter(
    (el) => el !== `id`
  );

  // Ensure custom rules are applied at the beginning
  python.contains.push(whiteTokens);
  python.contains.push(attributeTokens);
  python.contains.push(yellowTokens);

  return python;
});

hljs.highlightAll();
hljs.initLineNumbersOnLoad();
