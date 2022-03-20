process.stdin.setEncoding("utf8");
process.stdin.on("data", (data) => {
  const n = data.split(" ");
  const a = Number(n[0]),
    b = Number(n[1]);

  for (let y = 0; y < b; y++) {
    let star = "";

    for (let x = 0; x < a; x++) {
      star += "*";
    }

    console.log(star);
  }
});
