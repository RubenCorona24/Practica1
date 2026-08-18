import { describe, expect, test } from "vitest";
import { getHeroAction } from "../get-hero.action";


describe("getHeroAction", () => {
    test("should fetch hero data and return with complete image url", async () => {
        const result = await getHeroAction('clark-kent')
        const resultImageUrl = result.image
        console.log(result)
        expect(result).toBeDefined()
        expect(result).toStrictEqual({
            id: '1',
            name: 'Clark Kent',
            slug: 'clark-kent',
            alias: 'Superman',
            powers: [
                'Súper fuerza',
                'Vuelo',
                'Visión de calor',
                'Visión de rayos X',
                'Invulnerabilidad',
                'Súper velocidad'
            ],
            description: 'El Último Hijo de Krypton, protector de la Tierra y símbolo de esperanza para toda la humanidad.',
            strength: 10,
            intelligence: 8,
            speed: 9,
            durability: 10,
            team: 'Liga de la Justicia',
            image: 'http://localhost:3000',
            firstAppearance: '1938',
            status: 'Active',
            category: 'Hero',
            universe: 'DC'
        })
        expect(resultImageUrl).toContain("http")
    });
    {/*const mockHero = { //mockeamos al heroe
            "id": "2",
            "name": "Bruce Wayne",
            "slug": "bruce-wayne",
            "alias": "Batman",
            "powers": [
                "Artes marciales",
                "Habilidades de detective",
                "Tecnología avanzada",
                "Sigilo",
                "Genio táctico"
            ],
            "description": "El Caballero Oscuro de Ciudad Gótica, que utiliza el miedo como arma contra el crimen y la corrupción.",
            "strength": 6,
            "intelligence": 10,
            "speed": 6,
            "durability": 7,
            "team": "Liga de la Justicia",
            "image": "2.jpeg",
            "firstAppearance": "1939",
            "status": "Active",
            "category": "Hero",
            "universe": "DC"
        }
        vi.mocked(heroAPI.get).mockResolvedValue(mockHero)
        const result = await getHeroAction("bruce-wayne")
        expect(heroAPI.get).toHaveBeenCalledWith("/bruce-wayne")
        expect(heroAPI.get).toHaveBeenCalledTimes(1) //sea llamado una vez

        expect(result).toEqual({
            ...mockHero,
            image: `${import.meta.env.VITE_API_URL}/images/${mockHero.image}`
        })*/}

}),
    test("should throw an error if hero is not found", async () => {
        const idSlugWrong = "batman-2"
        await getHeroAction(idSlugWrong)
            .catch((error) => {
                console.log(error)
                expect(error).toBeDefined()
                expect(error.message).toBe("Request failed with status code 404")

            })

    })
