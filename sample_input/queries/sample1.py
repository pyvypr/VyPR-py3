verification_conf = {
  "app.main.views" : {
    "index" : [
      Forall(
        s = changes('a')
      ).Check(
        lambda s : (
          s('a')._in([0, 10])
        )
      )
    ]
  }
}
