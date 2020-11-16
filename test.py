from yattag import Doc, indent
import datetime
import bz2
from html5print import HTMLBeautifier


# write html header
def write_head(doc, tag, text, line):
    # read the header bz2 file
    with bz2.open("src_href.bz2", "rt") as fscript:
        textscript = fscript.read()
    srch = textscript.split("\n")

    # write the html head
    doc.asis("<!DOCTYPE html>")

    with tag("html", xmlns="http://www.w3.org/1999/xhtml"):
        with tag("head"):
            doc.stag("meta", charset="utf-8")
            doc.asis(
                '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
            )
            doc.stag("meta", name="date", content=str(datetime.date.today()))

            with tag("title"):
                text("Cell Free DNA WGBS Analysis Report")

            with tag("script", src=srch[0]):
                text()

            doc.stag(
                "meta", name="viewport", content="width=device-width, initial-scale=1"
            )

            with tag("link", href=srch[1], rel="stylesheet"):
                text()

            with tag("script", src=srch[2]):
                text()

            with tag("script", src=srch[3]):
                text()

            with tag("script", src=srch[4]):
                text()

            with tag("script", src=srch[5]):
                text()

            with tag("link", href=srch[6], rel="stylesheet"):
                text()

            with tag("script", src=srch[7]):
                text()

            with tag("script", src=srch[8]):
                text()

            with tag("link", href=srch[9], rel="stylesheet"):
                text()

            with tag("script", src=srch[10]):
                text()

            with tag("link", href=srch[11], rel="stylesheet"):
                text()

            with tag("script", src=srch[12]):
                text()

            with tag("style", type="text/css"):
                text("code{white-space: pre;}")

            with tag("style", type="text/css"):
                text(
                    """
                pre:not([class]) {
                    background-color: white;
                }
                """
                )

            with tag("script", type="text/javascript"):
                doc.asis(
                    """
                if (window.hljs) {
                hljs.configure({languages: []});
                hljs.initHighlightingOnLoad();
                if (document.readyState && document.readyState === "complete") {
                    window.setTimeout(function() { hljs.initHighlighting(); }, 0);
                }
                }
                """
                )

            with tag("style", type="text/css"):
                text(
                    """
                .title1 {
                    font-size: 40px;
                    font-family: Roboto;
                    font-weight: bold;
                    line-height: 53px;
                    color: #20262A;
                    opacity: 1;
                    }
                """
                )
                text(
                    """
                    .text1 {
                    font-size: 16px;
                    font-family: Roboto;
                    font-weight: 400;
                    line-height: 21px;
                    color: #20262A;
                    opacity: 1;
                    }
                    }
                """
                )
                text(
                    """
                    .text2 {
                        font-size: 14px;
                        font-family: Roboto;
                        font-weight: 500;
                        color: #171717;
                        opacity: 1;
                    }
                """
                )
                text(
                    """
                    .card1 {
                        width: 300px;
                        height: 40px;
                        background: rgba(0, 82, 204, 0.1);
                        border-radius: 8px;
                        float: left;
                        margin-right: 24px;
                        margin-bottom: 43px;
                        padding: 10px 24px 10px 20px
                    }
                """
                )
                text("h1 {\n  font size: 34px;\n}\n")
                text("h2 {\n  font size: 30px;\n}\n")
                text("h3 {\n  font size: 24px;\n}\n")
                text("h4 {\n  font size: 18px;\n}\n")
                text("h5 {\n  font size: 16px;\n}\n")
                text("h6 {\n  font size: 12px;\n}\n")
                text(".table th:not([align]) {\n  text-align: left;\n}")

            with tag("style", type="text/css"):
                text(
                    "\ntable.customize {\n	font-size:12px;\n	color:#333333;\n	border-width: 1px;\n	border-color: #888888;\n	border-collapse: collapse;\n}"
                )
                text(
                    "\ntable.customize th {\n	border-width: 1px;\n	padding: 8px;\n	border-style: solid;\n	border-color: #888888;\n}"
                )
                text(
                    "\ntable.customize td {\n	border-width: 2px;\n	padding: 6px;\n	border-left-style: none;\n	border-right-style: none;\n	border-top-style: solid;\n	border-bottom-style: solid;\n	border-color: #DFDFDF;\n}"
                )


# write body part
def write_body(doc, tag, text, line):
    with tag("body"):
        with tag("style", type="text/css"):
            text(
                "\n.main-container {\n  max-width: 940px;\n  margin-left: auto;\n  margin-right: auto;\n}"
            )
            text(
                "\ncode {\n  color: inferit;\n  background-color: rgba(0, 0, 0, 0.04);\n}"
            )
            text("\nimg {\n  max-width: 100%;\n  height: auto;\n}")
            text("\n.tabbed-pane {\n  padding-top: 12px;\n}")
            text("\nbutton.code-folding-btn:focus {\n  outling: none;\n}")

        # Main Title
        with tag("div", id="container", style="width:1280px;margin:0 auto;"):
            with tag(
                "div",
                style="background:rgba(0,0,0,1);;padding:10px 0px 0px 108px;height:100px;width:1280px;background:url(header.png);background-size:1280px 100px;background-repeat:no-repeat;position:fixed;z-index: 10",
            ):
                doc.stag(
                    "img",
                    src="logo.png",
                    style="margin-right:8px;width:36px;height:46.46px;float:left",
                )
                with tag(
                    "div",
                    style="float:left;margin-bottom:8px;color:white",
                    klass="title1",
                ):
                    text("Cell Free DNA WGBS Analysis Report")

                with tag("div", style="clear:both"):
                    with tag(
                        "div",
                        klass="text1",
                        style="margin-left:650px;margin-bottom:32px;color:white",
                    ):
                        text(str(datetime.date.today()))

        # TOC part, all parts are controlled by TOC
        with tag("div", klass="container-fluid main-container"):
            with tag("script"):
                doc.asis(
                    '\n$(document).ready(function () {\n  window.buildTabsets("TOC");\n});'
                )

            with tag("script"):
                doc.asis(
                    "\n$(document).ready(function ()  {\n\n    // move toc-ignore selectors from section div to header\n    $('div.section.toc-ignore')\n        .removeClass('toc-ignore')\n        .children('h1,h2,h3,h4,h5').addClass('toc-ignore');\n\n    // establish options\n    var options = {\n      selectors: \"h1,h2,h3\",\n      theme: \"bootstrap3\",\n      context: '.toc-content',\n      hashGenerator: function (text) {\n        return text.replace(/[.\\/?&!#<>]/g, '').replace(/\s/g, '_').toLowerCase();\n      },\n      ignoreSelector: \".toc-ignore\",\n      scrollTo: 0\n    };\n    options.showAndHide = true;\n    options.smoothScroll = true;\n\n    // tocify\n    var toc = $(\"#TOC\").tocify(options).data(\"toc-tocify\");\n});"
                )

            with tag("style", type="text/css"):
                text(
                    "\n#TOC {\n  margin: 125px 0px 20px 0px;\n}\n@media (max-width: 768px) {\n#TOC {\n  position: relative;\n  width: 100%;\n}\n}"
                )
                text(
                    "\n.toc-content {\n  padding-left: 30px;\n  padding-right: 40px;\n}"
                )
                text("\ndiv.main-container {\n  max-width: 1200px;\n}")
                text(
                    "\ndiv.tocify {\n  width: 20%;\n  max-width: 260px;\n  max-height: 85%;\n}"
                )
                text(
                    "\n@media (min-width: 768px) and (max-width: 991px) {\n  div.tocify {\n    width: 25%;\n  }\n}"
                )
                text(
                    "\n@media (max-width: 767px) {\n  div.tocify {\n    width: 100%;\n    max-width: none;\n  }\n}"
                )
                text("\n.tocify ul, .tocify li {\n  line-height: 20px;\n}")
                text(
                    "\n.tocify-subheader .tocify-item {\n  font-size: 0.90em;\n  padding-left: 25px;\n  text-indent: 0;\n}"
                )
                text("\n.tocify .list-group-item {\n  border-radius: 0px;\n}")

            with tag("div", klass="row-fluid"):
                with tag("div", klass="col-xs-12 col-sm-4 col-md-3"):
                    with tag("div", id="TOC", klass="tocify"):
                        text()

                with tag("div", klass="toc-content col-xs-12 col-sm-8 col-md-9"):
                    title_count = 1

                    # fastqc report
                    with tag(
                        "div",
                        id="fastqc_report",
                        klass="section level1",
                        style="margin:120px 20px 20px 20px",
                    ):
                        with tag("h1"):
                            with tag("span", klass="header-section-number"):
                                text(str(title_count) + ".")

                            text(" Fastq Quality Control")

                        text(
                            "The followings are quality control files generated by FastQC. For more detailed information, please click the hyperlinks below."
                        )

                        with tag(
                            "div",
                            id="fastqc_report_sub",
                            klass="section level2",
                            style="margin:20px",
                        ):
                            with tag("div", klass="card1"):
                                doc.stag(
                                    "img",
                                    src="FASTQ.png",
                                    style="cursor:pointer;height:20px;width:20px;float:left;margin-right:16px",
                                )
                                with tag("div", klass="text2", style="float:left"):
                                    text("TBR1448.read1_fastqc.html")
                                with tag("a", href="https://www.baidu.com/", target="_blank"):
                                    doc.stag(
                                        "img",
                                        src="Icon.png",
                                        style="cursor:pointer;margin-top:3px;height:14.14px;width:8.5px;float:right",
                                    )

                            with tag("div", klass="card1"):
                                doc.stag(
                                    "img",
                                    src="FASTQ.png",
                                    style="cursor:pointer;height:20px;width:20px;float:left;margin-right:16px",
                                )
                                with tag("div", klass="text2", style="float:left"):
                                    text("TBR1448.read1_fastqc.html")
                                with tag("a", href="https://www.baidu.com/", target="_blank"):
                                    doc.stag(
                                        "img",
                                        src="Icon.png",
                                        style="cursor:pointer;margin-top:3px;height:14.14px;width:8.5px;float:right",
                                    )

# start html creat
doc, tag, text, line = Doc().ttl()
write_head(doc, tag, text, line)
write_body(doc, tag, text, line)

# write output to html
prettyHTML = HTMLBeautifier.beautify(indent(doc.getvalue()), 4)
# prettyHTML = indent(doc.getvalue())

fout = open("test.html", "w")
fout.write(prettyHTML)
fout.close()
