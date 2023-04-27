import { render } from '@testing-library/react';
import { Tooltip } from 'components/Tooltip';

describe('Tooltip', () => {
    it('renders the tooltip content', () => {
        const content = 'Tooltip Content';
        const { getByText } = render(<Tooltip content={content} />);
        const tooltipContent = getByText(content);
        expect(tooltipContent).toBeInTheDocument();
    });

    it('renders the tooltip with the correct role', () => {
        const content = 'Tooltip Content';
        const { getByRole } = render(<Tooltip content={content} />);
        const tooltip = getByRole('tooltip');
        expect(tooltip).toBeInTheDocument();
    });

    it('renders the tooltip with the correct CSS classes', () => {
        const content = 'Tooltip Content';
        const { getByRole } = render(<Tooltip content={content} />);
        const tooltip = getByRole('tooltip');
        expect(tooltip).toHaveClass('left-1/5');
        expect(tooltip).toHaveClass('absolute');
        expect(tooltip).toHaveClass('top-12');
        expect(tooltip).toHaveClass('z-10');
        expect(tooltip).toHaveClass('rounded-sm');
        expect(tooltip).toHaveClass('bg-blue-500');
        expect(tooltip).toHaveClass('p-2');
        expect(tooltip).toHaveClass('text-sm');
        expect(tooltip).toHaveClass('text-white');
    });

    it('renders the tooltip arrow with the correct CSS classes', () => {
        const content = 'Tooltip Content';
        const { getByText, container } = render(<Tooltip content={content} />);
        const tooltipContent = getByText(content);
        const tooltipArrow = container.querySelector('.rotate-45');

        expect(tooltipContent).toBeInTheDocument();
        expect(tooltipArrow).toBeInTheDocument();
        expect(tooltipArrow).toHaveClass('pointer-events-none');
        expect(tooltipArrow).toHaveClass('absolute');
        expect(tooltipArrow).toHaveClass('bottom-full');
        expect(tooltipArrow).toHaveClass('left-[50%]');
        expect(tooltipArrow).toHaveClass('z-10');
        expect(tooltipArrow).toHaveClass('h-3');
        expect(tooltipArrow).toHaveClass('w-3');
        expect(tooltipArrow).toHaveClass('translate-x-[-50%]');
        expect(tooltipArrow).toHaveClass('translate-y-2');
        expect(tooltipArrow).toHaveClass('rotate-45');
        expect(tooltipArrow).toHaveClass('bg-blue-500');
    });
});
