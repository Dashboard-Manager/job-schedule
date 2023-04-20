type TextProps = {
    toggle: boolean;
    displayTxt: string;
};

const Text = ({ toggle, displayTxt }: TextProps) => {
    return <h1 data-testid="text">{toggle ? displayTxt : ''}</h1>;
};

export default Text;
