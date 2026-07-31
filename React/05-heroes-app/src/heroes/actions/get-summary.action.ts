import { heroAPI } from "../api/hero.api"
import type { SummaryInformationResponse } from "../interfaces/summary-information.response";

export const getSummaryAction = async () => {
    //desestructuramos la data de heroAPI
    const { data } = await heroAPI.get<SummaryInformationResponse>('/summary');
    //retornamos la data
    return data
}