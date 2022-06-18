const fs = require("fs");
const path = require("path");

// main code
(() => {
  let result = dirTree("Folang");
  fs.writeFileSync('output.json', JSON.stringify(result), 'utf8')
  printLeafs(result);
})();

// build json tree from folder
function dirTree(filename) {
  const stats = fs.lstatSync(filename),
    info = {
      path: filename,
      name: path.basename(filename),
      type: null,
      children: [],
    };

  if (stats.isDirectory()) {
    info.type = "folder";
    info.children = fs.readdirSync(filename).map(function (child) {
      return dirTree(filename + "/" + child);
    });
  } else {
    info.type = "file";
  }

  return info;
}

function printLeafs(node) {
  for (item of node.children) {
    if (!item.children.length) {
      console.log(item.path);
    }
    printLeafs(item);
  }
}
