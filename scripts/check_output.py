#!/usr/bin/env python3
"""Check built sites for broken internal links and missing image references.

Usage: check_output.py dist/arcanebyte
Exits non-zero if anything is broken, so it can gate a build.
"""
import os
import re
import sys

LINK = re.compile(r'<a[^>]*?href=(?:"([^"]+)"|([^\s>]+))', re.I)
IMG = re.compile(r'<img[^>]*?src=(?:"([^"]+)"|([^\s>]+))', re.I)
SKIP = ("http://", "https://", "mailto:", "tel:", "data:", "#")


def resolve(root, url):
    path = os.path.join(root, url.lstrip("/"))
    return os.path.isfile(path) or os.path.isfile(os.path.join(path, "index.html"))


def check(root):
    problems = []
    links = images = 0
    for base, _, names in os.walk(root):
        for name in names:
            if not name.endswith(".html"):
                continue
            page = os.path.join(base, name)
            html = open(page, encoding="utf-8").read()
            rel = os.path.relpath(page, root)

            for groups in LINK.findall(html):
                url = (groups[0] or groups[1]).split("#")[0]
                if not url or url.startswith(SKIP):
                    continue
                links += 1
                if not resolve(root, url):
                    problems.append(f"broken link  {url}  in {rel}")

            for groups in IMG.findall(html):
                url = groups[0] or groups[1]
                if not url or url.startswith(SKIP):
                    continue
                images += 1
                if not resolve(root, url):
                    problems.append(f"missing image  {url}  in {rel}")

    return links, images, problems


def main(roots):
    failed = False
    for root in roots:
        if not os.path.isdir(root):
            print(f"{root}: not built")
            failed = True
            continue
        links, images, problems = check(root)
        print(f"{root}: {links} links, {images} images, {len(problems)} problems")
        for problem in problems:
            print(f"    {problem}")
        failed = failed or bool(problems)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["dist/arcanebyte"]))
