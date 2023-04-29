type TooltipProps = {
    content: string;
};

export const Tooltip = ({ content }: TooltipProps) => {
    return (
        <div
            role='tooltip'
            className='left-1/5 absolute top-12 z-10 rounded-sm bg-blue-500 p-2 text-sm text-white'
        >
            {content}
            <div className='pointer-events-none absolute bottom-full left-[50%] z-10 h-3 w-3 translate-x-[-50%] translate-y-2 rotate-45 bg-blue-500' />
        </div>
    );
};
