from yattag import Doc, indent


def write_qualimap_report_contents(doc, tag, text, line, report, outputdir):
    report_dir, report_name = os.path.split(report)
    dstdir = outputdir + "/Qualimap/" + report_dir.split("/")[-1] + "/"
    if not os.path.exists(dstdir):
        os.makedirs(dstdir)
    for root, dirs, files in os.walk(report_dir):
        for file in files:
            src_file = os.path.join(root, file)
            shutil.copy(src_file, dstdir)
        for dir in dirs:
            subdir = os.path.join(root, dir)
            subdstdir = dstdir + "/" + dir
            if not os.path.exists(subdstdir):
                os.makedirs(subdstdir)
            for subroot, subdirs, subfiles in os.walk(subdir):
                for subfile in subfiles:
                    src_subfile = os.path.join(subdir, subfile)
                    shutil.copy(src_subfile, subdstdir)
        break
    shutil.copy(report, dstdir)

    with tag("div", klass="card1", style="display:block"):
        doc.stag(
            "img",
            src=os.path.join("./HTML_Elements", "icon_1.png"),
            style="cursor:pointer;height:20px;width:20px;float:left;margin-right:16px",
        )
        with tag("div", klass="text2", style="float:left"):
            text(report_name)
        with tag(
            "a",
            href="Qualimap/" + report_dir.split("/")[-1] + "/" + report_name,
            target="_blank",
        ):
            doc.stag(
                "img",
                src=os.path.join("./HTML_Elements", "icon_2.png"),
                style="cursor:pointer;margin-top:3px;height:14.14px;width:8.5px;float:right",
            )

    doc.stag("br")


doc, tag, text, line = Doc().ttl()

title_count += 1

with tag(
    "div",
    id="qualimap_report",
    klass="section level1",
    style="margin:20px",
):
    with tag("h1"):
        with tag("span", klass="header-section-number"):
            text(str(title_count) + ".")

        text(" Qualimap")

    text(
        "The followings are Qualimap reports. For more detailed information, please click the hyperlinks below."
    )
    for report in report_dir.getOutput("htmlOutput"):
        report_prev, report_name = os.path.split(report)
        with tag(
            "div",
            id="qualimap_report_sub",
            klass="section level2",
            style="margin:20px",
        ):
            with tag("h2"):
                text("Sample: " + report_prev.split("/")[-1])
            write_qualimap_report_contents(
                doc, tag, text, line, report, outputdir,
            )
