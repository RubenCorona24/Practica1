import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, test, vi } from "vitest";
import { CustomPagination } from "../CustomPagination";
import { MemoryRouter } from "react-router";

import type { PropsWithChildren } from "react";
import type React from "react";

vi.mock("@base-ui/react", () => ({
    Button: ({ children, ...props }: PropsWithChildren) => (
        <button {...props}>{children}</button>
    )
}))
//componente para envolver el router en el custompagination
const renderWithRouter = (children: React.ReactElement,
    initialEntries?: string[]
) => {
    return render(
        <MemoryRouter initialEntries={initialEntries}>
            {children}
        </MemoryRouter>

    )
}



describe("CustomPagination", () => {
    test("should render with default values", () => {
        const { container } = renderWithRouter(<CustomPagination totalPages={5} />)
        expect(container).toMatchSnapshot() //take a snapshot
    })
    test("should contain initial values", () => {
        renderWithRouter(<CustomPagination totalPages={5} />)
        expect(screen.getByText("Anteriores")).toBeDefined()
        expect(screen.getByText("Siguientes")).toBeDefined()
    })
    test("should disabled previous button when page is one", () => {
        const { container } = renderWithRouter(<CustomPagination totalPages={5} />)
        //take the previous button
        const previousButton = container.querySelector("button")
        expect(previousButton?.getAttributeNames()[1]).toBeDefined()
        expect(previousButton?.getAttributeNames()).toContain("disabled")
    })
    test("should disabled next button when we are in the last page", () => {
        renderWithRouter(<CustomPagination totalPages={5} />, ["/?page=5"])
        //take the next button
        const nextButton = screen.getByText("Siguientes")
        expect(nextButton.innerHTML).toContain("Siguientes")
        expect(nextButton.getAttributeNames()).toContain("disabled")

    })
    test("should disabled button 3 when we are in page 3", () => {
        renderWithRouter(<CustomPagination totalPages={10} />, ["/?page=3"])
        //take the next button
        const button2 = screen.getByText("2")
        const button3 = screen.getByText("3") //This button variant should be "default"

        screen.debug(button3)
        expect(button2.getAttribute("variant")).toBe("outline")
        expect(button3.getAttribute("variant")).toBe("default")


    })
    test("should change page when when click on number button", () => {
        renderWithRouter(<CustomPagination totalPages={5} />, ['/?page=3'])
        const button2 = screen.getByText("2")
        const button3 = screen.getByText("3")
        expect(button2.getAttribute("variant")).toBe("outline")
        expect(button3.getAttribute("variant")).toBe("default")
        fireEvent.click(button2)
        //make the same evaluations but reversely
        expect(button2.getAttribute("variant")).toBe("default")
        expect(button3.getAttribute("variant")).toBe("outline")
        screen.debug()

    })
})