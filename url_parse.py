url = "<url>https://xcdL32112.smart_meter.com</url>"
print("url:", url)
startIdx = 0
endIdx = 0
try:
    startIdx = url.index("https://")
    startIdx += 8
    print("https found at index:", startIdx)
except Exception as e:
    try:
        startIdx = url.index("http://")
        startIdx += 7
        print("http found at index:", startIdx)
    except ValueError:
        print("no http[s] found")

try:
    endIdx = url.index("</url>")
    print("</url> found at index:", endIdx)
except Exception as e:
    print("no </url> found")
else:
    print("Parsed url:", url[startIdx:endIdx])
