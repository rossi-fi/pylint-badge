def main():
    import argparse

    from pylint.lint import Run
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file_to_lint")
    args = parser.parse_args()
    file_to_lint = args.file_to_lint
    
    score = round(Run([file_to_lint], exit=False).linter.stats['global_note'], 2)
    
    template = '<svg xmlns="http://www.w3.org/2000/svg" width="85" height="20"><linearGradient id="a" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient><rect rx="3" width="85" height="20" fill="#555"/><rect rx="3" x="50" width="35" height="20" fill="{color}"/><path fill="{color}" d="M50 0h4v20h-4z"/><rect rx="3" width="85" height="20" fill="url(#a)"/><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11"><text x="25" y="15" fill="#010101" fill-opacity=".3">pylint</text><text x="25" y="14">pylint</text><text x="67" y="15" fill="#010101" fill-opacity=".3">{score}</text><text x="67" y="14">{score}</text></g></svg>'

    color_ok = "#44cc11"
    color_warning = "#dfb317"
    color_red = "#e05f44"
    
    if float(score) < 3.0:
        color = color_red
    elif float(score) >= 3.0 and float(score) < 7.0:
        color = color_warning
    else:
        color = color_ok
    
    with open("pylint.svg", 'w') as score_file:
        score_file.write(template.format(score=score, color=color))

if __name__ == "__main__":
    main()
