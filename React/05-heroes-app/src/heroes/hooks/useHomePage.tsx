import { useMemo } from "react";
import { useSearchParams } from "react-router";

export const useHomePage = () => {
    const [searchParams, setSearchParams] = useSearchParams()

    const activeTab = searchParams.get("tab") ?? 'all';
    const page = searchParams.get("page") ?? '1';
    const limit = searchParams.get("limit") ?? '6';
    const category = searchParams.get("category") ?? 'all';

    const selectedTab = useMemo(() => {
        const validTabs = ['all', 'favorites', 'heroes', 'villains']
        return validTabs.includes(activeTab) ? activeTab : 'all'
    }, [activeTab])


    return {
        //values
        page,
        limit,
        selectedTab,
        category,
        //methods
        setSearchParams
    }


}
