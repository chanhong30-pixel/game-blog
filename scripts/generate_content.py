rom datetime import datetime

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>🎮 游戏博主 · 自动更新</title>
  <meta name="description" content="由 GitHub Actions 自动生成的游戏内容">
</head>
<body style="font-family:Arial;max-width:900px;margin:40px auto;">
  <h1>🎮 游戏博主</h1>
  <p><em>自动生成时间：{now}</em></p>

  <article>
    <h2>今日游戏速览</h2>
    <p>这是由 GitHub Actions 自动生成的最新内容。</p>
    <ul>
      <li>新作情报与更新动态</li>
      <li>热门游戏趋势分析</li>
      <li>玩家社区讨论焦点</li>
    </ul>
  </article>

  <hr>
  <p style="color:#888;font-size:12px;">
    本页面每次 GitHub Actions 运行都会自动更新
  </p>
</body>
</html>
"""

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ public/index.html 已覆盖生成")
